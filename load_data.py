from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
import gradio as gr
from gradio.themes.base import Base
import genai

def load_data(dbName, collectionName):
    client = MongoClient(genai.MongoURI)
    collection = client[dbName][collectionName]
    loader = DirectoryLoader( './samples', glob="./*.txt", show_progress=True)
    data = loader.load()

    embeddings = OpenAIEmbeddings(openai_api_key=genai.openai_api_key)

    vectorStore = MongoDBAtlasVectorSearch.from_documents(data, embeddings, collection=collection)