from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import huffman
import shannon_fano
import json
import os
from datetime import datetime
import all
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

class DecompressInput(BaseModel):
    encoded_data:str
    codes:dict

@app.post("/compress")
def compress_text(input: TextInput):
    text = input.text

    result = all.compress_all(text)

    filename = f"compressed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    filepath = f"compressed/{filename}"
    os.makedirs("compressed", exist_ok=True)

    with open(filepath, "w") as f:
        json.dump({
            "huffman": {
                "encoded_data": result["huffman"]["encoded_data"],
                "codes": result["huffman"]["codes"]
            },
            "shannon_fano": {
                "encoded_data": result["shannon_fano"]["encoded_data"],
                "codes": result["shannon_fano"]["codes"]
            }
        }, f)

    return {
        "message": "Texto comprimido exitosamente.",
        "data": result,
        "download_url": f"/download/{filename}"
    }

@app.post("/decompress/huffman")
def decompress_huffman(input: DecompressInput):
    try:
        result = huffman.decompress(input.encoded_data, input.codes)
        return {"decoded_text": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/decompress/shannon_fano")
def decompress_shannon_fano(input: DecompressInput):
    try:
        result = shannon_fano.decompress(input.encoded_data, input.codes)
        return {"decoded_text": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/download/{filename}")
def download_file(filename: str):
    filepath = f"compressed/{filename}"
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    return FileResponse(path=filepath, filename=filename, media_type='application/json')