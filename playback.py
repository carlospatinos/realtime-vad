"""
Plays back some audio
"""

# Import packages
from pydub import AudioSegment
from pydub.playback import play
import sys


def capture(fileName):
    # Play audio
    playaudio = AudioSegment.from_file(fileName, format="wav")
    play(playaudio)


args = sys.argv[1:]
if len(args) != 1:
    sys.stderr.write(
        'Usage: playback.py <pathToFile>\n')
    quit()
else:
    capture(args[0])
