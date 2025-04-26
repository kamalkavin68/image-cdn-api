from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi import HTTPException
import shutil
import os

app = FastAPI()

IMAGE_DIR = "uploaded_images"

@app.get("/")
async def root():
    return {"detail": "API is running"}


@app.get("/images/{image_name}")
async def get_image(image_name: str):
    extension = os.path.splitext(image_name)[1]
    image_path = os.path.join(IMAGE_DIR, "equity", "png", image_name)
    if not os.path.exists(image_path):
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(image_path, headers={
        "Cache-Control": "public, max-age=31536000, immutable"
    })
