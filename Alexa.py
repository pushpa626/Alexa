import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = None  # Set command to None initially
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except Exception as e:  
        print("An error occurred:", e)
        return None  
    return command

def run_alexa():
    while True:
        command = take_command()
        print(command)
        if command is not None:
            if 'stop' in command:
                talk('Stopping Alexa')
                break 
            elif 'hello' in command or 'hey' in command:
                talk('Hello! Which song would you like to listen to?')
            elif 'play' in command:
                song = command.replace('play', '')
                talk('playing ' + song)
                pywhatkit.playonyt(song)
            else:
                talk('Please say the command again.')
        else:
            talk('An error occurred. Please try again.')

run_alexa()

