import matplotlib.pyplot as plt
import numpy as np
from statistics import mean
import wave
import sys

plt.figure(1)

class Audio:
    def __init__(self, audio):
        self.audio = wave.open(audio,'r')
        self.signal = self.audio.readframes(-1)
        self.signal = np.fromstring(self.signal, 'Int16')
        self.fr = self.audio.getframerate()
        self.time = np.linspace(0, 100, num=(len(self.signal)))
        self.fft = np.fft.fft(self.signal)

    def plot(self):
        plt.title("Audio waveforms")
        plt.plot(self.time, self.signal, '.')

m = Audio('input.wav')
w= Audio('w.wav')


m.plot()
plt.show()
w.plot()
plt.show()
