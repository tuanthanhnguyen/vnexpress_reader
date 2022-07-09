# Voice reader for [Vnexpress](https://vnexpress.net)
### Reader for articles on Vnexpress


## Install dependencies:
### ```ffmpeg```
Linux
```
$ sudo apt update
$ sudo apt install ffmpeg
```
Mac
```
brew install ffmpeg
```
Windows: grab binaries [here](https://ffmpeg.org/download.html) (add ffmpeg dir to PATH or else it won't work)
## Usage
```
git clone https://github.com/tuanthanhnguyen/vnexpress_reader.git
cd vnexpress_reader/src
pip install -r requirements.txt
python main.py
```
### **Note : Ensure config file "config.ini" is present in working directory**
## Config.ini options:

1. ```save_html_content``` (True/False) : Save vnexpress's response as HTML (debugging)
2. ```log_erors``` (True/False) : Log errors
3. ```save_article_text``` (True/False) : Save article as text (txt)
4. ```save_article_audio``` (True/False) : Save article as audio (mp3)
5. ```reader``` (vt/gtts) : Choose TTS provider (Viettel / Google Translate)
6. ```api_key``` (string) : Viettel AI API key (Leave blank if you don't have one)

### I'm using the demo version for both Viettel & Google TTS options. Please do not abuse their API.
### I strongly recommend you paste your API key into the ```config.ini``` file if you have one.