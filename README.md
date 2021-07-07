# realtime-vad
testing vad on realtime

python3 -V
Python 3.9.1

python3 -m pip install --user pipenv
sudo -H pip install -U pipenv

brew install portaudio

pipenv shell
pipenv install pyaudio
pipenv install wave
pipenv install sounddevice