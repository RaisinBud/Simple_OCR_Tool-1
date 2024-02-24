from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
import shutil
import ocr
#import ocrpython --version
import os
import uuid
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/ocr/config/")
def Config(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ocr/get-texts-for-images/")
async def Get_Texts_For_Images(image: UploadFile = File(...)):
    temp_file = _save_file_to_disk(image, path="temp", save_as="temp")
    text = await ocr.read_image(temp_file)
    return {"filename": image.filename, "text": text}

def _save_file_to_disk(uploaded_file, path=".", save_as="default"):
    extension = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path, save_as + extension)
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)
    return temp_file
