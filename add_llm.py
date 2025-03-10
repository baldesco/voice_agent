import dotenv
import os

import google.generativeai as genai
from fastrtc import ReplyOnPause, Stream, get_stt_model, get_tts_model

# Load env variables
dotenv.load_dotenv(".env.local")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash-lite")


sst_model = get_stt_model()
tts_model = get_tts_model()

chat = model.start_chat()


def echo(audio):
    prompt = sst_model.stt(audio)
    # Here you can call your LLM
    response = chat.send_message(prompt)
    response = response.text

    # Remove asterisks from the response
    response = response.replace("*", "")

    for audio_chunk in tts_model.stream_tts_sync(response):
        yield audio_chunk


stream = Stream(ReplyOnPause(echo), modality="audio", mode="send-receive")
stream.ui.launch()
