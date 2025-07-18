import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init()


def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

def main():
    recognizer = sr.Recognizer()

    print("AI Desktop Assistant: I can help you search on Google. Say 'exit' to quit.")

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            user_query = recognizer.recognize_google(audio).lower()
            print(f"You said: {user_query}")

            if user_query == 'exit':
                print("Goodbye!")
                break
            else:   
                search_google(user_query)

        except sr.UnknownValueError:
            print("Sorry, I did not understand. Please repeat.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("How can I assist you today?")
    
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Sorry, I couldn't understand that. Please try again.")
        return "None"
    return query

if __name__ == "__main__":
    greet_me()
    while True:
        
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
            
        elif "play the music" in query:
            music_dir = "F:\Python language\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
            
        elif "what is your name" in query:
            speak("My name is Speech recognition system.")  
            
        elif "what is your contribution" in query:
            speak("here is my role to respond all inquiries in human language in visual or voice format")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            
        elif 'google search' in query:
            speak('What do you want to search on Google?')
            search_query = take_command().lower()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'open whatsapp' in query:   
            webbrowser.open("https://web.whatsapp.com")
        
        elif 'open gniot erp' in query:
            webbrowser.open("https://web.gnioterp.com")

        elif 'open stack overflow' in query:
            webbrowser.open("https://www.stackoverflow.com")

        elif 'exit' in query:
            speak("Goodbye!")
            break
        elif 'surf google' or 'sirf google' or 'search google' in query:
            main()
            if 'exit' in query:
                break
            