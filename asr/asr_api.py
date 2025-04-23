from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from datasets import Dataset, Audio
import torch
import tempfile
import shutil
import soundfile as sf
from pydub.utils import mediainfo
import os

app = FastAPI()

# Load model and processor only once at startup
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")

@app.get("/ping")
async def ping():
    return {"response": "pong"}

@app.post("/asr")
async def transcribe(file: UploadFile = File(...)):
    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    try:
        # Load file into Huggingface Dataset
        ds = Dataset.from_dict({
            "audio": [tmp_path]
        }).cast_column("audio", Audio(sampling_rate=16000))

        # Process audio and get transcription
        input_values = processor(ds[0]["audio"]["array"], return_tensors="pt", padding="longest", sampling_rate=16000).input_values


        with torch.no_grad():
            logits = model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = processor.batch_decode(predicted_ids)[0]


        # Use pydub to calculate the duration
        audio_info = mediainfo(tmp_path)
        duration = audio_info.get('duration', 'Unknown')

        return JSONResponse(content={
            "transcription": transcription,
            "duration": duration
        })
    finally:
        os.remove(tmp_path)

# from venv
# uvicorn asr.asr_api:app --host 0.0.0.0 --port 8001

# Test the API with curl
# curl http://localhost:8001/ping
# curl -F "file=@/Users/neleht./Desktop/nosync/recent/common_voice/cv-valid-dev/cv-valid-dev/sample-000000.mp3" http://localhost:8001/asr