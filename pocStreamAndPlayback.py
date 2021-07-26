import sounddevice as sd
import audio2numpy as a2n

duration = 5.5  # seconds


# Input to Output Pass-Through
# Possibly use a queue to pass the data and detect data
def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata


def emergencyMessage(audioLocation):
    status = None
    try:
        data, fs = a2n.audio_from_file(audioLocation)
        sd.play(data, fs)
        status = sd.wait()
    except KeyboardInterrupt:
        print('\nInterrupted by user')
    except Exception as e:
        print(type(e).__name__ + ': ' + str(e))
    if status:
        print('Error during playback: ' + str(status))


emergencyMessage("./playback/emergencia.mp3")
with sd.RawStream(channels=2, dtype='int24', callback=callback):
    sd.sleep(int(duration * 1000))
emergencyMessage("./playback/emergencia.mp3")
with sd.RawStream(channels=2, dtype='int24', callback=callback):
    sd.sleep(int(duration * 1000))

print("No sound in the call")
