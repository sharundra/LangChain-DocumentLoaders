from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


loader = DirectoryLoader(
    path = "ray/",
    glob = "*.pdf",
    loader_cls = PyPDFLoader
)

#docs is just a generator which sits idle unless we 'poke' it to generate doc pages one by one.
docs = loader.lazy_load()

doc1 = next(docs) # this will force docs to generate the first page and then remove it from docs
print(f'the 1st page is :{doc1.page_content}')

doc2 = next(docs) # this will force docs to generate the second page and then remove it from docs
print(f'the 2nd page is :{doc2.page_content}')

# # the bad way to use lazy_load though it will work  and load all the docs' pages and completely empty docs
# all_docs = list(docs)
# print(f'Total page count is {len(all_docs)}')

# the good way to use lazy_load. here also, at the end, docs will be completely emptied
for doc in docs:
    print(f'The current page is :{doc.page_content}') 

# doc_check = next(docs)
# print(f'The current page is :{doc_check.page_content}')


