# HTX_xData_Assignment

git clone git@github.com:N313H/HTX_xData_Assignment.git

---

### Setup

1. Clone the repository
```bash
git clone git@github.com:N313H/HTX_xData_Assignment.git
```
2. Install requirement



# Task 2

This directory implements a microservice that hosts a pre-trained Automatic Speech Recognition (ASR) model (`wav2vec2-large-960h`) using FastAPI. It provides an endpoint to transcribe `.mp3` audio files and has been containerized using Docker.

Directory:
```
asr/
├── asr_api.py         # FastAPI microservice for ASR
├── cv-decode.py       # Script to transcribe Common Voice mp3s using the API
├── Dockerfile         # Docker container setup
└── requirements.txt   # Python dependencies
```

## Dockerization
1. Ensure all file paths are correctly defined

2. Build Docker image
```
docker build -t asr-api .
```

2. Run the container
```
docker run -p 8001:8001 asr-api
```

3. Test 

```
curl -F "file=@/Users/neleht./Desktop/nosync/HTX_xData_test/common_voice/cv-valid-dev/cv-valid-dev/sample-000000.mp3" http://localhost:8001/asr
```


# Task 3

Directory:
```
asr-train/
├── cv-train-2a.ipynb
```
1. Ensure all file paths are correctly defined
2. `cv-train-2a.ipynb` Run All

# Task 5

Directory:
```
hotword-detection/
├── cv-hotword-5a.ipynb # Hotword detection on transcriptions
├── cv-hotword-similarity-5b.ipynb # Semantic similarity detection using embeddings
├── detected.txt # List of audio files containing hotwords
├── cv-valid-dev.csv # Updated with similarity column
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

5. `cv-hotword-5a.ipynb`


   


