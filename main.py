from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi import HTTPException
import os

app = FastAPI()

EQUITY_IMAGE_DIR = "images/equity/png"
INDICES_IMAGE_DIR = "images/indices/png"

@app.get("/")
async def root():
    return {"detail": "API is running"}


@app.get("/images/equity/{image_name}")
async def get_equity_image(image_name: str):
    image_path = EQUITY_IMAGE_DIR + "/" + image_name
    print(f"Image path: {image_path}")
    if not os.path.exists(image_path):
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(image_path, headers={
        "Cache-Control": "public, max-age=31536000, immutable"
    })

@app.get("/images/indices/{image_name}")
async def get_indices_image(image_name: str):
    image_path = INDICES_IMAGE_DIR + "/" + image_name
    print(f"Image path: {image_path}")
    if not os.path.exists(image_path):
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(image_path, headers={
        "Cache-Control": "public, max-age=31536000, immutable"
    })
