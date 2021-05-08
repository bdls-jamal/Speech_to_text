import speech_recognition as sr
from tkinter import *
import sys
# import tkinter.font as tkFont
# import time
# import os
# from pydub import AudioSegment
# from pydub.silence import split_on_silence

'small audio files.'
# filename = "machine-learning_speech-recognition_16-122828-0002.wav"
# r = sr.Recognizer()
#
# with sr.AudioFile(filename) as source:
#     audio_data = r.record(source)
#     text = r.recognize_google(audio_data)
#     print(text)

r = sr.Recognizer()

'large audio files'


# def get_large_audio_transcription(path: object) -> str:
#     sound = AudioSegment.from_wav(path)
#     chunks = split_on_silence(sound, min_silence_len=500,
#                               silence_thresh=sound.dBFS-14, keep_silence=500)
#     folder_name = 'audio-chunks'
#
#     if not os.path.isdir(folder_name):
#         os.mkdir(folder_name)
#     whole_text = ""
#
#     for i, audio_chunk in enumerate(chunks, start=1):
#         chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
#         audio_chunk.export(chunk_filename, format="wav")
#
#         with sr.AudioFile(chunk_filename) as source:
#             audio_listened = r.record(source)
#             try:
#                 text = r.recognize_google(audio_listened)
#             except sr.UnknownValueError as e:
#                 print("Error:", str(e))
#             else:
#                 text = f"{text.capitalize()}."
#                 print(chunk_filename, ":", text)
#                 whole_text += text
#
#     return whole_text
#
#
# file = "machine-learning_speech-recognition_7601-291468-0006.wav"
# print("\nFull text:", get_large_audio_transcription(file))

'Microphone to Text'


# def microphone_to_text(languages: dict, language_codes: dict) -> None:
#     languages_text = ''
#     for language in languages:
#         languages_text += f'{language}: {languages[language]}\n'
#
#     with sr.Microphone() as source:
#         # read the audio data from the default microphone
#         lang = language_codes[input(languages_text)]
#         print('Start talking now.')
#         audio_data = r.record(source, duration=5)
#         print("Recognizing...")
#         # convert speech to text
#         text = r.recognize_google(audio_data, language=lang)
#         print(text)
#         time.sleep(2)
#         again = input('Would you like to try again? \n1: Yes \n2: No')
#         if again == '1':
#             microphone_to_text(languages, language_codes)
#         else:
#             exit()


language_dict = {'1': 'English', '2': 'Japanese'}
language_dict_code = {'1': 'en-EN', '2': 'ja'}
# microphone_to_text(language_dict, language_dict_code)


def english():
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=5)
        # convert speech to text
        text = r.recognize_google(audio_data, language='en-En')
        display_text(text)


def japanese():
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=5)
        # convert speech to text
        text = r.recognize_google(audio_data, language='ja')
        display_text(text)


def display_text(text: str):
    label.update()
    label.configure(text='')
    label2.update()
    label2.configure(text=f'{text}')
    label2.place(relx=0.475, rely=0.3, anchor=CENTER)
    btn0.update()
    btn0.configure(text='Retry', command=reset)
    btn1.update()
    btn1.configure(text='Exit', command=sys.exit)

    # exit_btn.update()
    # exit_btn.configure(text='Exit', command=exit_func)
    # exit_btn.place(relx=0.5, rely=0.5, anchor=S)


def message_ja():
    label.update()
    label.configure(text='Speak now...')
    label.place(relx=0.475, rely=0.3, anchor=CENTER)
    window.after(100, japanese)


def message_en():
    label.update()
    label.configure(text='Speak now...')
    label.place(relx=0.475, rely=0.3, anchor=CENTER)
    window.after(100, english)


def reset():
    label2.update()
    label2.configure(text='')
    window.after(200, clicked)


def clicked():
    btn0.update()
    btn0.configure(text="English", command=message_en)
    btn0.place(relx=0.4, rely=0.5, relwidth=0.1, relheight=0.1)
    btn1.update()
    btn1.configure(text='Japanese', command=message_ja)
    btn1.place(relx=0.5, rely=0.45, relwidth=0.1, relheight=0.1)


window = Tk()
window.option_add("*font", "Times 15")
window.title("Speech to Text Converter")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
# window.geometry("%dx%d" % (width, height))
window.geometry("900x600")

btn0 = Button(window, text="Start", command=clicked)
btn0.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.1, relheight=0.1)
btn1 = Button(window, text='')
exit_btn = Button(window, text='Exit', command=sys.exit)
label = Label(window, text='')
label2 = Label(window, text='')

window.mainloop()
