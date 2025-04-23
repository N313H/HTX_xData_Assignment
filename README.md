# HTX_xData_Assignment

git clone git@github.com:N313H/HTX_xData_Assignment.git

---

### Setup

1. **Clone the repository**
```bash
git clone git@github.com:N313H/HTX_xData_Assignment.git
```


# ASR Microservice – Task 2

This directory implements a microservice that hosts a pre-trained Automatic Speech Recognition (ASR) model (`wav2vec2-large-960h`) using FastAPI. It provides an endpoint to transcribe `.mp3` audio files and has been containerized using Docker.

asr/
├── asr_api.py         # FastAPI microservice for ASR
├── cv-decode.py       # Script to transcribe Common Voice mp3s using the API
├── Dockerfile         # Docker container setup
└── requirements.txt   # Python dependencies


## Directory Structure

