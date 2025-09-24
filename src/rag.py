
from langchain_core.documents import Document
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings


from langchain.text_splitter import RecursiveCharacterTextSplitter
from llama_cpp import Llama

from langchain.retrievers.contextual_compression import ContextualCompressionRetriever

import re

def clean_text(text):
    text = re.sub(r'[*_`\\]+', '', text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text
from langchain.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
from langchain_cohere import CohereRerank

from langchain_cohere import CohereEmbeddings
compressor = CohereRerank(model="rerank-english-v3.0")
class Retriver():
    def __init__(self,majors_url="/mnt/c/Users/klyme/Downloads/majors.jsonl"):
        self.majors=[]
        self.doc_store={}
        with open(majors_url, 'r', encoding="Windows-1252") as majors:
            id=0
            for major in majors:                
                self.doc_store[id]=major
                major=self.create_document(major, id)

                self.majors.append(major)
                id+=1       
        self.embeddings= CohereEmbeddings(model="embed-v4.0")
    def retrieve_docs(self, query):
        self.db=FAISS.from_documents(self.majors, self.embeddings).as_retriever(search_kwargs={'k':10})
        compression_retriever = ContextualCompressionRetriever(
            base_compressor=compressor, base_retriever=self.db
        )
    
        compressed_docs = compression_retriever.invoke(query)

        return compressed_docs
    
    def split_chunks(self,doc, id):
        tokenizer = self.from_pretrained("google-bert/bert-base-uncased")

        text_splitter=RecursiveCharacterTextSplitter(
            chunk_size=300, 
            chunk_overlap=50, 
            length_function=lambda x : len(tokenizer(x)['input_ids']), 
            is_separator_regex=False
        )

        chunks=text_splitter.create_documents(texts=[doc], metadatas=[{'id': id}])

        return chunks

    def create_document(self,doc, id):
        d=doc.encode('latin1').decode('utf-8')
        clean= d.replace('�', '')

        txt=clean_text(clean)
        return Document(page_content=txt, metadata={'id' : id})

    def __call__(self, query):
        retrieved_docs=self.retrieve_docs(query)
        print(retrieved_docs)
        results=' '.join([doc.page_content for doc in retrieved_docs])
        return results



class RAG():
    def __init__(self, model_path="/mnt/c/Users/klyme/Downloads/Qwen3-14B-Q4_K_M.gguf"):
        self.llm=Llama(model_path=model_path, n_ctx=8000, n_batch=512, n_gpu_layers=-1)

    def _run_query(self, profile):
        retriver=Retriver()
        context=retriver(profile)
        prompt = f"Given the profile: {profile} and the three majors: {context}, carefully evaluate and compare each major against the profile: consider strengths, interests, values, and likely career fit; weigh trade-offs and choose the single best match. Respond ONLY in this exact format:\\n\\nRecommended Major: [major name]\\nReasoning: Explicitly link 3–4 key traits from the profile to 3–4 quoted supporting phrases from the chosen major's description (use single quotes). Write 4–5 concise sentences explaining why the major is the best fit, balancing technical, creative, and interpersonal factors. If multiple majors are close, prefer the one that offers stronger long-term growth or fills important skill gaps. Do NOT include internal chain-of-thought or any extra text—output only the two required lines."
        
        response=self.llm.create_chat_completion(messages=[
            {'role':'system', 'content': 'You are a career advisor AI'}, 
            {'role':'user', 'content':f'{prompt}'}
        ], max_tokens=2048)

        self.llm.close() 
        return response['choices'][0]['message']["content"].strip()
    def __call__(self, profile):
        return self._run_query(profile)


profile="""Your Hard Skills': Based on your answers, your technical strengths are evident in several areas. You have a solid foundation in mathematics, as indicated by your enjoyment of solving mathematical problems (Question 2) and your self-identification as a good mathematician (Question 6). However, you express some limitations with computers, stating that you are not particularly good with them (Question 2). Additionally, while you have some comfort with managing tasks, your reluctance to lead or organize people (Question 8) suggests that your hard skills may be more aligned with individual contributions rather than team leadership or project management. Overall, your mathematical abilities and task management capabilities stand out, while your comfort with technology may require further development.
'Your Soft Skills': Your interpersonal strengths appear to be more nuanced. While you generally feel comfortable working in teams (Question 1), you also enjoy solitude at times. This suggests that you may thrive in collaborative environments but also appreciate independence. In terms of emotional intelligence, you note that your understanding of others' feelings can depend on the situation (Question 5), indicating a developing ability to connect with others. You also express some resilience in managing stress (Question 3), though your reluctance to adapt quickly may challenge this strength in high-pressure situations. Your interest in learning about languages and cultures (Question 7) suggests a curiosity that enhances your adaptability in diverse environments. However, your hesitance to lead and organize may indicate that your soft skills are more supportive of team dynamics rather than proactive leadership.
'Your Overall Profile': Combining your hard and soft skills, you present as a mathematically inclined individual who enjoys working independently or in teams, depending on the situation. You are adaptable in managing stress but may need to develop your ability to adapt to unforeseen changes more effectively. While you are not particularly drawn to medical or technological fields, your curiosity about languages and cultures opens avenues for exploration. Your reluctance to lead suggests that you may be more comfortable contributing as part of a team rather than taking charge, which might influence your career choices. Overall, you are a thoughtful and analytical person who values independence and has a keen interest in cultural pursuits"""


major="""Data Science is a dynamic field designed for individuals who possess a strong analytical mindset, a keen curiosity for uncovering insights from data, and a collaborative spirit. Ideal candidates for this major are those who take pleasure in tackling complex problems, have a propensity for critical thinking, and are comfortable navigating both quantitative and qualitative data. Students who thrive in this discipline often exhibit a blend of technical proficiency and creativity, allowing them to not only analyze data but also to visualize and communicate their findings effectively.
Throughout the Data Science program, students develop a comprehensive set of technical skills and domain knowledge essential for data-driven decision-making. The curriculum includes courses in statistical analysis, machine learning, data mining, and programming languages such as Python and R. Students learn to work with various data tools and platforms, including SQL databases, cloud computing resources, and data visualization software like Tableau or Power BI. They also engage in hands-on projects that deepen their understanding of data wrangling, model building, and algorithmic thinking, equipping them with the expertise to extract actionable insights from large datasets.
In addition to technical competencies, the program emphasizes the cultivation of vital soft skills that are critical for success in the field. Effective communication, teamwork, and the ability to convey complex data narratives to diverse audiences are integral components of the curriculum. Students develop empathy, enabling them to understand user needs and contextualize their findings within real-world scenarios. Those who are detail-oriented, adaptable, and possess a natural inclination toward continuous learning will find themselves particularly well-suited to thrive in this rapidly evolving landscape.
Data Science education is not just about theory; it is firmly rooted in practical application. Students engage in collaborative projects, internships, and case studies that simulate real-world data challenges faced by organizations across various sectors. This hands-on approach prepares graduates to apply their knowledge in meaningful ways, allowing them to bridge the gap between technical solutions and business needs. 
As they complete their studies, graduates of the Data Science program are poised to embark on diverse career paths that involve harnessing data to drive innovation, improve processes, and inform strategic decisions. Whether through developing predictive models, optimizing operations, or providing actionable insights, they are equipped to make impactful contributions in an array of industries, effectively shaping the future of data utilization in society.
"""


llm=Llama(model_path="/mnt/c/Users/klyme/Downloads/codellama-7b-instruct.Q4_0.gguf", n_ctx=9000, n_batch=512, n_gpu_layers=-1)


prompt=f"Given user's profile:{profile}, and a university major that was chosen for him: {major}, generate an appropriate answer why is the major suiting for the user. Link user's personal strengths from his profile, and use information from the given major to structure a coherent reply"


prompt=f"""You are an expert career advisor. Your task is to generate a personalized explanation of why a suggested college major suits a specific user. 

Instructions:
1. Read the user's profile carefully. Highlight their hard and soft skills, interests, and preferences.
2. Read the description of the suggested major. Understand its technical requirements, soft skills needed, and potential career paths.
3. Write a clear, professional summary that explains why the major fits the user. 
4. Make explicit links between the user's strengths and aspects of the major.
5. Use details from both inputs but summarize in 6-8 sentences. Avoid repeating the full description of the major.

User Profile:
{profile}

Suggested Major:
{major}

Output:"""

response=llm(prompt, max_tokens=2048, echo=False)

print(response['choices'][0]['text'])

llm.close()
