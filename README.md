# HTX_xData_Assignment

---

### Setup

1. Clone the repository
```
git clone git@github.com:N313H/HTX_xData_Assignment.git
```
2. Install `requirements_all.txt`
```
pip install -r requirements_all.txt
```

3, Download `common_voice` data

---
# Task 2 - deploy an Automatic Speech Recognition (ASR) AI model for audio transcription

This directory implements a microservice that hosts a pre-trained Automatic Speech Recognition (ASR) model (`wav2vec2-large-960h`) using FastAPI. It provides an endpoint to transcribe `.mp3` audio files and has been containerized using Docker.

Directory:
```
asr/
├── asr_api.py         # FastAPI microservice for ASR
├── cv-decode.py       # Script to transcribe Common Voice mp3s using the API
├── Dockerfile         # Docker container setup
├── cv-valid-dev_task2.csv # Final csv file/ output for task 2
└── requirements.txt   # Python dependencies
```
## 2c) - hosted inference API for the model
1. Ensure all file paths are correctly defined
2. ```uvicorn asr.asr_api:app --host 0.0.0.0 --port 8001```
3. Run `cv-decode.py `
   

## 2e) Dockerization
1. Ensure all file paths are correctly defined
2. Build Docker image
```
docker build -t asr-api .
```
3. Run the container
```
docker run -p 8001:8001 asr-api
```
4. Test 
```
curl -F "file=@/Users/neleht./Desktop/nosync/HTX_xData_test/common_voice/cv-valid-dev/cv-valid-dev/sample-000000.mp3" http://localhost:8001/asr
```

---
# Task 3 - finetune an Automatic Speech Recognition (ASR) AI model

Directory:
```
asr-train/
├── cv-train-2a.ipynb
├── cv-valid-dev_task4.csv
├── cv-valid-dev_task4_final.csv # Final csv file/ output for task 4
├── cv-valid-test_task3-eval.csv # Final csv file/ output for task 3
├── cv-valid-test_task3.csv
├── duration_cache_file.csv
└── losses.csv
```
1. Ensure all file paths are correctly defined
2. Run All `cv-train-2a.ipynb` 

Due to limitations of git and github I was unable to upload my saved finedtuned model as it was too large. Instaed in its place I have attached a pdf with a link to Google drive to download the model. 
Link here: https://drive.google.com/file/d/1AsPgutXIlbJwYS6G8X28Y7zbRMzKKuaM/view?usp=sharing

---

# Task 5 - hot word and similarity detection

Directory:
```
hotword-detection/
├── cv-hotword-5a.ipynb # Hotword detection on transcriptions
├── cv-hotword-similarity-5b.ipynb # Semantic similarity detection using embeddings
├──cv-valid-dev-updated.csv # Final csv file/ output for task 5b
├── requirements_instructor.txt
└── detected.txt # List of audio files containing hotwords for task 5a

```

1. Ensure all file paths are correctly defined
2. Start up a virtual environment (python3.10 latest)
```
python3.10 -m venv venv
source venv/bin/activate
venv\Scripts\activate
```
3. Install  `requirement_instructor.txt`
```
pip install -r requirement_instructor.txt
```
4. Run All `cv-hotword-5a.ipynb` 
5. Run All `cv-hotword-similarity-5b.ipynb` 


   


