
from langchain_core.documents import Document
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings


from langchain.text_splitter import RecursiveCharacterTextSplitter
from llama_cpp import Llama

from langchain.retrievers.contextual_compression import ContextualCompressionRetriever


from langchain.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer

from langchain_cohere import CohereEmbeddings

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
        self.db=FAISS.from_documents(self.majors, self.embeddings).as_retriever(search_kwargs={'k':3})

        compressed_docs = self.db.invoke(query)

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
        return Document(page_content=doc, metadata={'id' : id})

    def __call__(self, query):
        retrieved_docs=self.retrieve_docs(query)
        results=' '.join([doc.page_content for doc in retrieved_docs])
        return results

prof="**Your Hard Skills**\n\nBased on your responses, you demonstrate notable strengths in several technical areas:\n\n1. **Business and Economics (Question 6)**: You expressed a strong interest in analyzing markets, managing money, and running projects, scoring a perfect 100. This indicates a solid foundation in business principles and economic reasoning, which could be beneficial in various business-related fields.\n\n2. **Creativity and Innovation (Question 7)**: Your enthusiasm for generating new ideas and experimenting with them, also receiving a score of 100, highlights a strong creative ability. This skill is essential in roles that require innovative thinking and problem-solving.\n\n3. **Technology (Question 2)**: While you noted that you do not particularly enjoy solving mathematical problems with computers, your general liking for technology (scoring 65) suggests a comfort level with tech tools that could be leveraged in various contexts.\n\nOverall, your hard skills primarily align with business acumen and creativity, which could be vital for roles in entrepreneurship, project management, or marketing.\n\n**Your Soft Skills**\n\nYour interpersonal and emotional strengths are reflected in the following areas:\n\n1. **Adaptability and Stress Management (Question 3)**: You indicated that you mostly can adapt when things don�t go as planned, yet noted that stress affects you (65). This suggests that while you are capable of managing change and uncertainty, you may benefit from developing further stress management techniques.\n\n2. **Emotional Intelligence and Empathy (Question 5)**: Your response reflects moderate ability to understand others' feelings, scoring 50. This indicates potential for developing deeper emotional intelligence, which is critical for effective teamwork and leadership.\n\n3. **Teamwork and Communication (Question 1)**: You feel mostly comfortable working in teams but also appreciate working alone at times (65). This shows that you can collaborate effectively while also valuing independent work.\n\nYour soft skills indicate a foundation in adaptability and teamwork, balanced by a need for further development in emotional intelligence and stress management.\n\n**Your Overall Profile**\n\nYou possess a unique blend of hard and soft skills that positions you well for various pathways. Your strong inclination towards business and creativity indicates a propensity for innovative thinking and project management. While you exhibit comfort in team settings, you also appreciate independent work, suggesting versatility in your working style. Your moderate emotional intelligence suggests that with targeted development, you could enhance your rapport with others�an asset in roles that require collaboration.\n\nHowever, it is important to acknowledge that stress management and deeper emotional understanding are areas where you could grow. Developing strategies to handle stress effectively could enhance your adaptability and overall performance in high-pressure situations.\n\n**Possible Career-Study Directions**\n\nConsidering your strengths, you might explore the following broad pathways:\n\n1. **Business Management and Entrepreneurship**: Your interests in market analysis and project management suggest that you could thrive in business-oriented programs that emphasize innovation and strategic thinking.\n\n2. **Creative Industries**: With your strong creativity and interest in bringing ideas to life, you could consider fields such as marketing, advertising, or product development, where both creativity and business insights are invaluable.\n\n3. **Technology and Management**: Given your comfort with technology and desire to analyze markets, you might explore technology management or digital marketing roles, where analytical skills and technological familiarity are crucial.\n\n4. **Social Sciences and Communication**: If you choose to further develop your emotional intelligence and teamwork abilities, a focus on social sciences or communication could provide you with the skills necessary to excel in collaborative environments.\n\nIn summary, your profile showcases a dynamic individual with a firm grasp on business principles and creative thinking, ready to explore various pathways that leverage these strengths while also keen on personal growth in emotional and stress management areas."   



class RAG():
    def __init__(self, model_path="/mnt/c/Users/klyme/Downloads/codellama-7b-instruct.Q4_0.gguf"):
        self.llm=Llama(model_path=model_path, n_ctx=4096, n_batch=512, n_gpu_layers=-1)

    def _run_query(self, profile):
        retriver=Retriver()
        context=retriver(profile)
        prompt = f"Given the profile: {profile} and the three majors: {context}, choose only one the most suitable university major and briefly explain why, based on user's profile. Analyze strengths, interests, values, and career fit, balancing technical, creative, and interpersonal factors. In 1–3 concise sentences explicitly link 1–2 profile traits to 1–2 short supporting phrases or section headings from the context (quote them in single quotes). Respond ONLY in this exact format (no extra text):\\n\\nRecommended Major: [major name]\\nReasoning: link profile traits to the chosen major and name the supporting context phrases. Make a rich-description of why the major suits the user (4-5 sentences)"
        
        response=self.llm.create_chat_completion(messages=[
            {'role':'system', 'content': 'You are a career advisor AI'}, 
            {'role':'user', 'content':f'{prompt}'}
        ], max_tokens=1024)

        self.llm.close() 
        return response['choices'][0]['message']["content"].strip()
    def __call__(self, profile):
        return self._run_query(profile)

rag=RAG()

print(rag(prof))