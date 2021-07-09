from pydub import AudioSegment
import sys
import os


def capture(pathToFile):
    filename, file_extension = os.path.splitext(pathToFile)
    sound = AudioSegment.from_file(pathToFile)

    print("----------Before Conversion--------")
    print("Frame Rate", sound.frame_rate)
    print("Channel", sound.channels)
    print("Sample Width", sound.sample_width)

    # Change Frame Rate
    sound = sound.set_frame_rate(16000)

    # Change Channel
    sound = sound.set_channels(1)

    # Change Sample Width
    sound = sound.set_sample_width(2)

    # Export the Audio to get the changed content
    sound.export(filename + "-transformed" + file_extension, format="wav")


args = sys.argv[1:]
if len(args) != 1:
    sys.stderr.write(
        'Usage: transform.py <pathToFile>\n')
    quit()
else:
    capture(args[0])
