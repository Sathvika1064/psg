import pytube
import moviepy.editor as mp
import ffmpeg
import speech_recognition as sr
import shutil
from gtts import gTTS
from googletrans import Translator
from pytube import YouTube
import os
def get_language_code(language_name):
    language_dict = {
    'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar',
    'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be',
    'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',
    'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn',
    'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr',
    'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
    'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi',
    'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka',
    'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht',
    'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi',
    'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig',
    'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja',
    'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km',
    'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo',
    'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb',
    'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml',
    'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn',
    'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or',
    'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt',
    'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm',
    'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn',
    'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl',
    'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw',
    'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th',
    'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug',
    'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh',
    'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
    return language_dict.get(language_name.lower())
def download_audio_wav(url, output_path,target_language):
    # Get the YouTube video stream with audio only
    target_language=get_language_code(target_language)
    video = pytube.YouTube(url)
    audio_stream = video.streams.filter(only_audio=True).first()

    if audio_stream:
        # Download the audio file
        audio_file_path = audio_stream.download()

        # Convert the audio to WAV format
        audio_clip = mp.AudioFileClip(audio_file_path)
        audio_clip.write_audiofile(output_path, codec="pcm_s16le")

        # Remove the original downloaded audio file
        audio_clip.close()
        mp.os.remove(audio_file_path)
        print("Audio downloaded and saved in WAV format successfully.")
        transcript = transcribe_audio("output_audio.wav")
        print(target_language)
        download_video(url)
        translated_text = translate_text(transcript, target_language)
        output_file = "output.mp3"
        output_file=convert_text_to_speech(translated_text, output_file,target_language)
        print("conversion done")

    else:
        print("No audio stream available for the video.")
def transcribe_audio(audio_path):
    r = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_path) as audio_file:
        audio = r.record(audio_file)  # Read the entire audio file

    # Perform speech recognition
    text = r.recognize_google(audio)  # Use Google Speech Recognition

    return text
def translate_text(text, target_language):
    translator = Translator()
    try:
        if text:
            translation = translator.translate(text, dest=target_language)
            return translation.text
        else:
            return None
    except Exception as e:
        print("Translation Error:", e)
        return None
def convert_text_to_speech(text, output_file,target_language):
    tts = gTTS(text=text, lang=target_language)
    tts.save(output_file)
    print("Audio file generated successfully.")
    source_file = 'output.mp3'
    #destination_folder = 'https://drive.google.com/drive/folders/1YkevND6TUyOa7d8O20vsPmtVvAr5K1iJ?usp=drive_link/'  # Replace with your desired destination folder
    try:
        print("Output audio file saved successfully!")
    except Exception as e:
        print("Error occurred while saving the output audio file:", str(e))

    return output_file
def download_video(url):
    path = path = r"C:\Users\DELL"
    url = "https://www.youtube.com/watch?v=GyQjVtIGQg8"
    resol = "1080p"
    file_type = "mp4"
    video = YouTube(url)
    Streams = video.streams
    vid = Streams.filter(res = resol, file_extension = file_type).first()
    new_file_path = os.path.join(path, "output_video.mp4")
    vid.download(new_file_path)


