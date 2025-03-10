from fastrtc import Stream, ReplyOnPause
import numpy as np

def echo(audio: tuple[int, np.ndarray]) -> tuple[int, np.ndarray]:
    yield audio

stream = Stream(ReplyOnPause(echo), modality="audio", mode="send-receive")
stream.ui.launch()
