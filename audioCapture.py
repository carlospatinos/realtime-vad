import pyaudio
import wave
import sys


"""
Records input stream information from microphone and save it to wav file under audio folder.
"""
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5


def capture(fileName):
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording. ")
    print("* file generated in " + fileName)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(fileName, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


args = sys.argv[1:]
if len(args) != 1:
    sys.stderr.write(
        'Usage: audioCapture.py <outputFileName>\n')
    quit()
else:
    capture("audio/" + args[0] + ".wav")
