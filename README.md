# realtime-vad
testing vad on realtime

python3 -V
Python 3.9.1

python3 -m pip install --user pipenv
sudo -H pip install -U pipenv

brew install portaudio

# Steps to process audio
All files will be stored on audio folder with the filename as a wav file

```sh
pipenv shell
pipenv install 
python audioCapture.py <fileName>
python playback.py <pathToFile>
python plotAudio.py <pathToFile>
python transform.py <pathToFile>
python silenceremove.py <aggressiveness> <fileName>
python plotAudio.py <pathToNewFileWithSilenceRemoved>
```

https://ngbala6.medium.com/audio-processing-and-remove-silence-using-python-a7fe1552007a