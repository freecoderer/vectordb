from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
import gradio as gr
from gradio.themes.base import Base
import genai
from langchain_community.chat_models import ChatOpenAI

def delete_all_documents(dbName, collectionName):
    client = MongoClient(genai.MongoURI)
    collection = client[dbName][collectionName]

    # Delete all documents
    collection.delete_many({})

    # Check if the collection is now empty
    if not collection.count_documents({}) == 0:
        print("[오류] 여전히 Atlas내에 문서가 남아있습니다 프로그램을 종료합니다")