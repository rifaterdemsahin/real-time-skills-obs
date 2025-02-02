import speech_recognition as sr

def recognize_speech():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Speak into your microphone...")
        
        # Adjust for ambient noise and record the audio
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")

            # Write the recognized text to a file
            with open("transcription.txt", "a") as file:
                file.write(text + "\n")
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
    while True:
        recognize_speech()
        print("Press Ctrl+C to exit...")