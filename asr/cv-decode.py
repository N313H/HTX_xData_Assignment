import pandas as pd
import requests
import os
from tqdm import tqdm

# Path setup
CSV_PATH = "../common_voice/cv-valid-dev.csv"
AUDIO_BASE_PATH = "../common_voice/cv-valid-dev/"

API_URL = "http://localhost:8001/asr"

# Read the CSV
df = pd.read_csv(CSV_PATH)

# Prepare a list to store transcriptions
generated_texts = []
durations = []

# Loop over all audio files and send to ASR API
for filename in tqdm(df["filename"], desc="Transcribing"):
    audio_path = os.path.join(AUDIO_BASE_PATH, filename)
    
    try:
        with open(audio_path, "rb") as f:
            response = requests.post(API_URL, files={"file": f})
        if response.status_code == 200:
            transcription = response.json().get("transcription", "")
            duration = response.json().get("duration", "")
            print(f"filename: {filename}")
        else:
            transcription = f"[ERROR {response.status_code}]"
    except Exception as e:
        transcription = f"[EXCEPTION] {str(e)}"
    
    generated_texts.append(transcription)
    durations.append(duration)

# Add the new column to DataFrame
df["generated_text"] = generated_texts
df["duration"] = durations

# Save the updated CSV
OUTPUT_CSV_PATH = "cv-valid-dev_task2.csv"
df.to_csv(OUTPUT_CSV_PATH, index=False)

print(f"\n Transcriptions saved to {OUTPUT_CSV_PATH}")

""""
# Testing the ASR API with a smaller subset
df_test = df.head(5).copy()

# Run ASR only on this subset
generated_texts = []
for filename in tqdm(df_test["filename"], desc="Transcribing first 5"):
    audio_path = os.path.join(AUDIO_BASE_PATH, filename)
    try:
        with open(audio_path, "rb") as f:
            response = requests.post(API_URL, files={"file": f})
        if response.status_code == 200:
            transcription = response.json().get("transcription", "")
            print(f"filename: {filename}")
        else:
            transcription = f"[ERROR {response.status_code}]"
    except Exception as e:
        transcription = f"[EXCEPTION] {str(e)}"
    generated_texts.append(transcription)

df_test["generated_text"] = generated_texts

# Save test results
df_test.to_csv("cv-valid-dev_first5_with_generated_text.csv", index=False)"""

# in file directory
# python3 cv-decode.py
