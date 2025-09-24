
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
    


import json

# Path to your JSONL file
file_path = r"/mnt/c/Users/klyme/Downloads/dataset (2).jsonl"

labels=[]

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        obj = json.loads(line)       # Parse each line into a Python dict
        label = obj.get("label")     # Access the "label" field
        labels.append(label)


print(len(labels))