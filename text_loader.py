from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

loader = TextLoader('satyajit_ray_legacy.txt')
doc_obj = loader.load()

print(doc_obj)
print(f'type of doc_obj: {type(doc_obj)}')
print(f'length of doc_obj: {len(doc_obj)}')
print(f' main content of doc_obj: {doc_obj[0].page_content}')  # print(doc_obj[0].page_content)
print(f' metadata of doc_obj: {doc_obj[0].metadata}')  # print(doc_obj[0].metadata)

model = ChatOpenAI()

output_parser = StrOutputParser()

prompt = PromptTemplate(template="Summarize this text: {text}", input_variables=["text"])

chain = prompt | model | output_parser

print(f' Summary of the input text : {chain.invoke(doc_obj[0].page_content)}')