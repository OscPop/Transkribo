
# Transkribo
This project revolves around using OpenAI's speech-to-text model **Whisper** to transcribe audio into text. Whisper is a lot better at transcribing Swedish audio than the current built-in transcription capabilities of Microsoft Teams. The downside of using whisper is that it doesn't know who's speaking at a given time, unlike Teams which has knowledge of different audio inputs (people in a Teams meeting/call). 

By combining whisper with the automatic transcription from Microsoft Teams, we get accurate transcriptions with accurate speaker classification. 


## Installation
The libraries used in this project are presented in `requirements.txt`. To install them, navigate to a virtual environment and activate it. Then type `python -m pip install -r requirements.txt` to install all the libraries. 
<br><br>
You will need to have `whisper` installed on your system to run this code. An installation guide for whisper is available at: https://github.com/openai/whisper.
<br><br>
You will probably also need to have `ffmpeg` installed on your system.


