# Requirements
For this to work on your device, it requires the installation of pyaudio and SpeechRecognition.
These can be downloaded via the command line using pip or your preferred alternative method.
Note that pyaudio requires Microsoft Visual C++ 14.0.

# The Code
This is the first version of my speech to text program.
It takes input from the user's microphone and converts it into text which is then presented on screen.
Works almost flawlessly in a quiet environment, moderately well with minor background noise and poorly with background noise louder than the user.
It uses packages: tkinter, speech_recognition and sys.
Currently supports Japanese and English voice input however simply changing a few areas of the code can allow it to support other languages.

# Future Use
This small program is intented to be used towards a much larger AI used for realistic conversation practice.
The idea is to train an AI to be able to take user input and respond with phrases that make sense in regular conversation in multiple languages.
This idea is inspired by my desire to practice speech in the Japanese language as a native English speaker in a controlled environment and without having to seek out native Japanese speakers for help.

# NOTICE
There is audio file to text conversion functions commented out within the code, this is to remain commented or deleted and is solely for personal reference and potential future use.
Code cleanup and GUI changes to come.

# ENJOY!
To anybody who sees this, I hope you get a kick out of using it!
