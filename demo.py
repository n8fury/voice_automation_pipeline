import numpy as np
from scipy.io import wavfile
import pyaudio

def sound(array, fs=8000):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=len(array.shape), rate=fs, output=True)
    stream.write(array.tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()


def record(duration=3, fs=8000):
    nsamples = duration*fs
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=fs, input=True,
                    frames_per_buffer=nsamples)
    buffer = stream.read(nsamples)
    array = np.frombuffer(buffer, dtype='int16')
    stream.stop_stream()
    stream.close()
    p.terminate()
    return array


# fs, data = wavfile.read('do.wav')
# sound(data, fs=4000)

my_recording = record()
sound(my_recording)

print(type(my_recording))
