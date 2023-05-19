
# Transkribo
This project revolves around using OpenAI's speech-to-text model **Whisper** to transcribe audio into text. Whisper is a lot better at transcribing Swedish audio than the current built-in transcription capabilities of Microsoft Teams. The downside of using whisper is that it doesn't know who's speaking at a given time, unlike Teams which has knowledge of different audio inputs (people in a Teams meeting/call). 

By combining whisper with the automatic transcription from Microsoft Teams, we get accurate transcriptions with accurate speaker classification. 


## Languages
The model is not limited to the Swedish language. The following graphic is taken from the official [OpenAI whisper](https://github.com/openai/whisper) repository. It shows the WER-score (word error rate) on the [Fleurs](https://huggingface.co/datasets/google/fleurs) dataset using the largest whisper model, `large-v2`. The smaller the WER score, the better.
<img src="Images/openai-whisper-language-breakdown.svg">


## Specs
Most of the work was done on a laptop with XXX.


## Files and folders
The different aspects of the project are presented in various jupyter notebooks for a more interactive walkthrough with comments and help along the way.




## Installation
The libraries used in this project are presented in `requirements.txt`. To install them, navigate to a virtual environment and activate it. Then type `python -m pip install -r requirements.txt` to install all the libraries. 
<br><br>
You will need to have `whisper` installed on your system to run this code. An installation guide for whisper is available at the official [whisper repository](https://github.com/openai/whisper).
<br><br>
You will probably also need to have `ffmpeg` installed on your system. You can put the executable (.exe file) inside the root directory, and the code should be able to find and use it. 





### Whisper versions
I've tried several different versions of whisper from the OpenAI GitHub page, but the later versions did not perform as good as the 20230124 version (at least for the Swedish interviews I tried on). The translation quality might have been more accurate for the later versions, but the sentences were cut short most of the time. 

#### Whisper model
From empirical tests, I've concluded that the `large-v2` model is the best OpenAI-whisper model for transcribing Swedish audio. Unfortunately though, it is also the slowest ... 
<br>
There are faster solutions out there but for my use case, this seemed like the best at the time. OpenAI even has a whisper API, but if we want to run the code locally and not end up in a cloud somewhere, we can't use their API.
<br>
Examples of other solutions:
1. [Whisper-jax](https://github.com/sanchit-gandhi/whisper-jax)
2. [OpenAI whisper API](https://platform.openai.com/docs/models/whisper)
3. [Ggerganov whisper.cpp](https://github.com/ggerganov/whisper.cpp)


## Finding the right parameters
It is difficult to figure out which parameters are the optimal ones since there is no ground-truth to automatically compute the performance of a specific model. The evaluation is currently done by visually inspecting the output in terms of accuracy, spelling, sentence length and coherence.


## Future ideas
There are instances where a teams transcription is not available, for instance when the interview (or any audio file for that matter) was done outside of Teams. In this case whisper will only allow us to get the transcribed speech, and we can't assign speaker labels for the speech segments. To deal with these cases, I tried experimenting a bit with automatic speaker recognition. The speaker recognition just needed to be told how many speakers were present in the audio and it would assign each speech segment with a tag such as "speaker 1". One could then go in afterwards and map the speakers with their real names. The speaker recognition was not that reliable however.

### Sensitive information
An advantage of being able to use the models locally on your own computer and having a reliable speaker recognition in place, is the possibility of using it to transcribe audio that is considered confidential or sensitive. The audio could be processed and treated in an isolated environment. 


## Other solutions
There are other version of whisper out there, and OpenAI even has a whisper API available. If we want to run the code locally and not end up in a cloud somewhere, we can't use their API.


## Fixing teams audio/text misalignment
Teams transcriptions aren't perfectly aligned with actual speech, sometimes the difference was more than 20s. Fortunately, the misalignment was constant in all the cases I encountered. This means I could put a constant offset to either the speech or the text to align them again. 

### Automatically fixing alignment
I did not spend that much time looking into how to automatically find the offset in milliseconds, instead I listened to a couple of seconds of each audio snippet to hear what the difference was. Manually listening to the audio ensures that it becomes correct.
<br>
An automatic solution might include listening to the first words in the audio and then trying to get an accurate timestamp from the speech-to-text model. The thing with whisper however, is that it sometimes removes/shortens words and sentences - which might affect the timestamp. 
<br>
Just taking the first "non-silent" audio as the start of the speech is not a good solution either as the audio could be some background noise.
