from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


loader = DirectoryLoader(
    path = "ray/",
    glob = "*.pdf",
    loader_cls = PyPDFLoader
)

docs = loader.load()

print(len(docs))
print(type(docs))
print(f'the page content of 23rd page in overall pages : {docs[22].page_content}')
print(f'the metadata of 23rd page in overall pages : {docs[22].metadata}')

