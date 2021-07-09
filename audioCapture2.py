"""
Not working
"""

import webrtcvad
vad = webrtcvad.Vad()
vad.set_mode(1)


def main(file, agresividad):

    audio, sample_rate = read_wave(file)
    vad = webrtcvad.Vad(int(agresividad))
    frames = frame_generator(30, audio, sample_rate)
    frames = list(frames)
    segments = vad_collector(sample_rate, 30, 300, vad, frames)
    for i, segment in enumerate(segments):
        path = 'chunk-%002d.wav' % (i,)
        print(' Writing %s' % (path,))
        write_wave(path, segment, sample_rate)


if __name__ == '__main__':
    file = 'audio/silenceWithVoice.wav'
    agresividad = 3  # aggressiveness
    main(file, agresividad)
