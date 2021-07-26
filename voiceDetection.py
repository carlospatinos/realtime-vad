#!/usr/bin/env python3
"""
Process microphone input stream endlessly.
The streaming of the input by the underlying sounddevice library
might take ~7% of a single i7 processor's utilization, before
any processing of ours.

With the vad model employed, it's around ~40% of a single cpu's time.
Luckily we have multi-core machines these days ...
"""

import sys
import time
import sounddevice as sd
# required to avoid crashing in assigning the callback input which is a numpy object
import numpy as np
import webrtcvad
import audio2numpy as a2n

emergencyDetectionDuration = 5.5  # seconds
voiceDetection = False

channels = [1]
# translate channel numbers to be 0-indexed
mapping = [c - 1 for c in channels]

# get the default audio input device and its sample rate
device_info = sd.query_devices(None, 'input')
sample_rate = int(device_info['default_samplerate'])

interval_size = 30  # audio interval size in ms
downsample = 1

block_size = sample_rate * interval_size / 1000

# get an instance of webrtc's voice activity detection
vad = webrtcvad.Vad()

print("reading audio stream from default audio input device:\n" +
      str(sd.query_devices()) + '\n')
print(F"audio input channels to process: {channels}")
print(F"sample_rate: {sample_rate}")
print(F"window size: {interval_size} ms")
print(F"datums per window: {block_size}")
print()


def emergencyMessage(audioLocation):
    print("Playing emergency audio")
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


def voice_activity_detection(audio_data):
    return vad.is_speech(audio_data, sample_rate)


def audio_callback(indata, frames, time, status):
    global voiceDetection
    # if voiceDetection == True:
    #     print("Audio already detected")
    #     return
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(F"underlying audio stack warning:{status}", file=sys.stderr)

    assert frames == block_size
    # possibly downsample, in a naive way
    audio_data = indata[::downsample, mapping]
    # normalize from [-1,+1] to [0,1], you might not need it with different microphones/drivers
    audio_data = map(lambda x: (x+1)/2, audio_data)
    # adapt to expected float type
    audio_data = np.fromiter(audio_data, np.float16)

    # uncomment to debug the audio input, or run sounddevice's mic input visualization for that
    #print(f'{sum(audio_data)} \r', end="")
    #print(f'min: {min(audio_data)}, max: {max(audio_data)}, sum: {sum(audio_data)}')

    audio_data = audio_data.tobytes()

    voiceDetection = voice_activity_detection(audio_data)
    # use just one line to show the detection status (speech / not-speech)
    print(f'Voz detectada?: {voiceDetection} \r', end="")
    # if voiceDetection:
    #     print("Audio detected redirecting to real agent -> :)")


def detectEmergencyFromStream():
    with sd.InputStream(
            device=None,  # the default input device
            channels=max(channels),
            samplerate=sample_rate,
            blocksize=int(block_size),
            callback=audio_callback):
        sd.sleep(int(emergencyDetectionDuration * 1000))
        # avoid shutting down for endless processing of input stream audio
        # while True:
        #     time.sleep(0.1)  # intermittently wake up


emergencyMessage("./playback/emergencia.mp3")
detectEmergencyFromStream()
emergencyMessage("./playback/emergencia.mp3")
detectEmergencyFromStream()
