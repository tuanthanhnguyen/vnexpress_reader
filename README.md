# Voice reader for [Vnexpress](https://vnexpress.net)
### Reader for articles on Vnexpress

## Usage:
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