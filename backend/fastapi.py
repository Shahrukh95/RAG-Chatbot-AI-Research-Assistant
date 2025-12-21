from fastapi import FastAPI, UploadFile
import os

app = FastAPI()

# CREATE/GET "uploads" FOLDER
CURRENT_PATH = os.getcwd()
UPLOADED_DIR = "backend/data/uploads"
upload_folder = os.path.join(CURRENT_PATH, UPLOADED_DIR)
os.makedirs(upload_folder, exist_ok=True)

@app.post("/ingest")
async def save_file(files: list[UploadFile]):
    saved_files =[]
    for file in files:
        contents = await file.read()

        filename = file.filename
        save_path = os.path.join(upload_folder, filename)

        try:
            with open(save_path, "wb") as f:
                f.write(contents)
            saved_files.append(filename)
        except Exception as e:
            return {"error": f"Failed to save {filename}: {str(e)}"}

    return {"files-saved": saved_files}