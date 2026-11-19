from utils.audio_processor import process_input
from core.transcriber import transcribe_all

source = "https://youtu.be/jnP9AgtX0qo?si=GZwAzK6BRiLQ1x_5"

chunks = process_input(source)

print(transcribe_all(chunks))