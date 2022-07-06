# Import the json library
import json
import os
import requests, time
from text_preprocessing import process
from moviepy.editor import concatenate_audioclips, AudioFileClip
from shutil import move
def concatenate_audio_moviepy(audio_clip_paths, output_path):
    """Concatenates several audio files into one audio file using MoviePy
    and save it to `output_path`. Note that extension (mp3, etc.) must be added to `output_path`"""
    clips = [AudioFileClip(c) for c in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)
    final_clip.write_audiofile(output_path)
def vt_recognize(filename,indata,token):
    headers = {'Content-type': 'application/json', 'token': token}
    paths = []
    saved_str = ""
    data = process(indata,500)
    for i in data:
        saved_str += i
    with open("result.txt", "w", encoding="utf-8") as outfile:
        outfile.write(saved_str)
    for count, text in enumerate(data):
        json_data = {
        'text': text,
        'voice': 'hn-quynhanh',
        'id': '3',
        'without_filter': False,
        'speed': '1.0',
        'tts_return_option': 3,
        'timeout': 60000,
            }
        response = requests.post('https://viettelgroup.ai/voice/api/tts/v1/rest/syn', headers=headers, json=json_data)
        print(response.headers)
    # Get status_code.
        print(response.status_code)
    # Get the response data as a python object.
        content = response.content
        path = "./chunks/" + str(count) + '.mp3'
        paths.append(path)
        with open(path, 'wb') as soundfile:
            soundfile.write(content)
        print(f"Recognised (index {count})")
        time.sleep(1)
    concatenate_audio_moviepy(paths,"full.mp3")
    move("./full.mp3", filename)
    for file in paths:
        os.remove(file)