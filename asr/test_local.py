from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from datasets import Dataset, Audio
import torch
from pydub.utils import mediainfo

# Load model and processor
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")

audio_file_path = "/Users/neleht./Desktop/HTX Technical Test/HTX_xData_test/common_voice/cv-valid-test/cv-valid-test/sample-000002.mp3"

# Load local MP3 file
ds = Dataset.from_dict({
    "audio": [audio_file_path]
}).cast_column("audio", Audio(sampling_rate=16000))

# Tokenize
input_values = processor(ds[0]["audio"]["array"], return_tensors="pt", padding="longest").input_values  # Batch size 1

# Retrieve logits
with torch.no_grad():  # optional, prevents gradient computation
    logits = model(input_values).logits

# Take argmax and decode
predicted_ids = torch.argmax(logits, dim=-1)
transcription = processor.batch_decode(predicted_ids)

# Use pydub to calculate the duration
audio_info = mediainfo(audio_file_path)
duration = audio_info.get('duration', 'Unknown')

# Print transcription and duration
print("Transcription:", transcription)
print("Duration (seconds):", duration)
print("Dataset:", ds)
