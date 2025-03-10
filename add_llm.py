import os

from fastrtc import ReplyOnPause, Stream, get_stt_model, get_tts_model
# from openai import OpenAI

sst_model = get_stt_model()
tts_model = get_tts_model()


def echo(audio):
    prompt = sst_model.stt(audio)
    # Here you can call your LLM
    response = f"""
You asked this: {prompt}
My answer is: who cares!
"""
    for audio_chunk in tts_model.stream_tts_sync(response):
        yield audio_chunk


stream = Stream(ReplyOnPause(echo), modality="audio", mode="send-receive")
stream.ui.launch(share=True)
