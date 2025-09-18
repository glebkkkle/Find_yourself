
from langchain_core.documents import Document
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

from langchain.text_splitter import RecursiveCharacterTextSplitter
from llama_cpp import Llama

from langchain.retrievers.document_compressors import CohereRerank
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_community.embeddings import CohereEmbeddings
from langchain_cohere import CohereEmbeddings

import cohere
co = cohere.Client("9qyTOO9RLCI6n4j7CMHVFNd4rnNfwoJQz4pmzqTk")

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
        self.embeddings=CohereEmbeddings(model="embed-v4.0")

    def retrieve_docs(self, query):
        self.db=FAISS.from_documents(self.majors, self.embeddings).as_retriever(search_kwargs={'k':3})
        
        compression_retriever = ContextualCompressionRetriever(base_compressor=compressor, base_retriever=self.db)
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

profile="Do you feel comfortable working in team? (Communication + Teamwork) - Mostly, but sometimes alone (65,25); Do you enjoy solving mathematical problems with computer? (Tech + Analytical) - Not Really, but like technologies (65,25); Are you comfortable adapting quickly when things don't go as planned? (Adaptivity + Stress Management) - Mostly, but stress affects me (65,25); Are you interested in learning how the human body or nature works? (Medical + Natural Sciences) - Sometimes, It depends (50,50); Do you usually understand what others feel and how to respond emotionally? (Emotional Intelligence + Empathy) - Sometimes, It depends (50,50); Do you enjoy analyzing markets, managing money, or running projects? (Business + Economics) - Yes, It's really interests me (100,100); Do you often come up with new ideas and enjoy experimenting with them? (Creativity + Innovation) - Yes, I'm very creative (100,100); Do you enjoy writing, learning languages, or exploring culture and history? (Language + Social Studies) - Mostly, but I prefer learning languages only (65,25); Do you enjoy leading people and organizing processes or tasks? (Leadership + Self-Management) - Sometimes, It depends (50,50); Do you like working with visuals, sounds, or building artistic things? (Creative + Applied Arts) - Not Really, but I can bring others' ideas to life (25,65)"

rag=RAG()

print(rag(profile))