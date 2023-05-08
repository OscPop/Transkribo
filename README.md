
# Transkribo
This project revolves around using OpenAI's speech-to-text model **Whisper** to transcribe audio into text. Whisper is a lot better at transcribing Swedish audio than the current built-in transcription capabilities of Microsoft Teams. The downside of using whisper is that it doesn't know who's speaking at a given time, unlike Teams which has knowledge of different audio inputs (people in a Teams meeting/call). 

By combining whisper with the automatic transcription from Microsoft Teams, we get accurate transcriptions with accurate speaker classification. 


## Specs
Most of the work was done on a laptop with XXX.


## Files and folders
The different aspects of the project are presented in various jupyter notebooks for a more interactive walkthrough.


## Installation
The libraries used in this project are presented in `requirements.txt`. To install them, navigate to a virtual environment and activate it. Then type `python -m pip install -r requirements.txt` to install all the libraries. 
<br><br>
You will need to have `whisper` installed on your system to run this code. An installation guide for whisper is available at: https://github.com/openai/whisper.
<br><br>
You will probably also need to have `ffmpeg` installed on your system.


### Whisper versions
I've tried several different versions of whisper from the OpenAI GitHub page, but the later versions did not perform as good as the 20230124 version (at least for the Swedish interviews I tried on). The translation quality might have been more accurate for the later versions, but the sentences were cut short most of the time. 


## Finding the right parameters
It is difficult to figure out which parameters are the optimal ones since there is no ground-truth to automatically compute the performance of a specific model. The evaluation is currently done by visually inspecting the output in terms of accuracy, spelling, sentence length and coherence.


## Future ideas
There are instances where a teams transcription is not available, for instance when the interview (or any audio file for that matter) was done outside of Teams. In this case whisper will only allow us to get the transcribed speech, and we can't assign speaker labels for the speech segments. To deal with these cases, I tried experimenting a bit with automatic speaker recognition. The speaker recognition just needed to be told how many speakers were present in the audio and it would assign each speech segment with a tag such as "speaker 1". One could then go in afterwards and map the speakers with their real names. The speaker recognition was not that reliable however.

### Sensitive information
An advantage of being able to use the models locally on your own computer and having a reliable speaker recognition in place, is the possibility of using it to transcribe audio that is considered confidential or sensitive. The audio could be processed and treated in an isolated environment. 