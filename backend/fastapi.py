from fastapi import FastAPI, UploadFile
import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from .content_parser import *

app = FastAPI()

# CREATE/GET "uploads" FOLDER
CURRENT_PATH = os.getcwd()
UPLOADED_DIR = "backend/data/uploads"
upload_folder = os.path.join(CURRENT_PATH, UPLOADED_DIR)
os.makedirs(upload_folder, exist_ok=True)

@app.post("/ingest")
async def save_file(files: list[UploadFile]):
    saved_files = []
    for file in files:
        contents = await file.read()

        filename = file.filename
        save_path = os.path.join(upload_folder, filename)

        # 1. Save PDFs
        try:
            with open(save_path, "wb") as f:
                f.write(contents)
            saved_files.append(filename)
        except Exception as e:
            return {"error": f"Failed to save {filename}: {str(e)}"}

        # 2. Chunk Files
        text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            model_name="gpt-4",
            chunk_size = 100,
            chunk_overlap = 20
        )

        pages = extract_text_and_images_by_page(pdf_path=save_path)
        metadatas = [{"filename": filename, "page": i+1} for i in range(len(pages))]
        chunked_text = text_splitter.create_documents(texts=pages, metadatas=metadatas)
        # print(chunked_text[0])


    # print(type(texts))
    # print(len(texts))
    return {"files-saved": saved_files, "output": chunked_text[-5:]}

