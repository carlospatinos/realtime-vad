"""
Plots the graph of audio
"""

from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt
import sys


def capture(fileName):
    # Read the Audiofile
    samplerate, data = read(fileName)
    # Frame rate for the Audio
    print(samplerate)

    # Duration of the audio in Seconds
    duration = len(data)/samplerate
    print("Duration of Audio in Seconds", duration)
    print("Duration of Audio in Minutes", duration/60)

    time = np.arange(0, duration, 1/samplerate)

    # Plotting the Graph using Matplotlib
    plt.plot(time, data)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title(fileName)
    plt.show()


args = sys.argv[1:]
if len(args) != 1:
    sys.stderr.write(
        'Usage: plotAudio.py <pathToFile>\n')
    quit()
else:
    capture(args[0])
