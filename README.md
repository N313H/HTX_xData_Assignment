# HTX_xData_Assignment

git clone git@github.com:N313H/HTX_xData_Assignment.git

---

### Setup

1. **Clone the repository**
```bash
git clone git@github.com:N313H/HTX_xData_Assignment.git
```

*** Change file paths to your local file paths ***


# ASR Microservice – Task 2

This directory implements a microservice that hosts a pre-trained Automatic Speech Recognition (ASR) model (`wav2vec2-large-960h`) using FastAPI. It provides an endpoint to transcribe `.mp3` audio files and has been containerized using Docker.

```
asr/
├── asr_api.py         # FastAPI microservice for ASR
├── cv-decode.py       # Script to transcribe Common Voice mp3s using the API
├── Dockerfile         # Docker container setup
└── requirements.txt   # Python dependencies
```

## Dockerization
```
docker build -t asr-api .
docker run -p 8001:8001 asr-api
```

Test with 

```
curl -F "file=@/Users/neleht./Desktop/nosync/HTX_xData_test/common_voice/cv-valid-dev/cv-valid-dev/sample-000000.mp3" http://localhost:8001/asr
```


