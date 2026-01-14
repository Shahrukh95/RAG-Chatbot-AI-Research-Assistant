from content_parser import *  # or import specific functions/classes


from langchain_text_splitters import RecursiveCharacterTextSplitter

# with open("backend/data/uploads/file1.pdf", "wb") as f:
#     state_of_the_union = f.read()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20, length_function=len, is_separator_regex=False,)
texts = text_splitter.create_documents(extract_text_and_images_by_page("backend/data/uploads/file2.pdf"))

print(f"{texts[0]} \n\n\n\n")
print(texts[1])

