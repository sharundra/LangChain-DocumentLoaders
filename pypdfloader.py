from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Religion of India in 6th century BC (Part 1).pdf')

doc = loader.load()

print(len(doc)) 
print(type(doc))
print(doc[2].page_content)
print(doc[2].metadata)


