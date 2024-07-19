from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
import gradio as gr
from gradio.themes.base import Base
import genai
import time
import sys
from langchain_openai import ChatOpenAI

def query_data(query, dbName, collectionName):
	client = MongoClient(genai.MongoURI)
	collection = client[dbName][collectionName]

	embeddings = OpenAIEmbeddings(openai_api_key=genai.openai_api_key)

	vectorStore = MongoDBAtlasVectorSearch(collection, embeddings)

	# Initialize a counter for the number of retries
	retry_count = 0

	print(f"Query: {query}")
	print(f"Database Name: {dbName}")
	print(f"Collection Name: {collectionName}")
	print(f"MongoURI: {genai.MongoURI}")
	print(f"Number of documents in the collection: {collection.count_documents({})}")

	# Loop until similarity_search returns at least one document or 30 seconds have passed
	while True:
		docs = vectorStore.similarity_search(query, K=1)
		if docs or retry_count >= 6:
			break
		print("문서를 받아오는 중입니다... 조금만 더 기달려주세요")
		time.sleep(5)
		retry_count += 1

	# If no documents were found after 30 seconds, terminate the function
	if not docs:
		print("[치명적 결함 발생] 30초가 지나도록 문서를 받아오지 못했습니다 프로그램을 종료합니다")
		sys.exit()

	as_output = docs[0].page_content

	# Create a new instance of the chatbot for each query
	llm = ChatOpenAI(openai_api_key=genai.openai_api_key, temperature=0, model_name="gpt-4-vision-preview")
	retriever = vectorStore.as_retriever()
	qa = RetrievalQA.from_chain_type(llm, chain_type="stuff", retriever=retriever)
	retriever_output = qa.invoke(query)

	return retriever_output['result']
