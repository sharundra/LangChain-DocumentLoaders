from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template = "Answer this below question \n {question} \n based on this following text {text}",
    input_variables = ["question", "text"]
)

model = ChatOpenAI()

output_parser = StrOutputParser()

loader = WebBaseLoader("https://www.reddit.com/r/OpenAI/comments/190122b/in_praise_of_dzmitry_bahdanau_who_in_2014/")

docs = loader.load()

chain = prompt | model | output_parser

result = chain.invoke({"question": "why is Dzmitry Bahdanau so great?",
              "text": docs[0].page_content
              })

#  print(f'length of docs : {len(docs)}')
print(f'Answer to the question : {result}')