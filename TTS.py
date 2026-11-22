import speech_recognition as sr

import pyttsx3


from googletrans import Translator


def speak(text, lang="en"):

    engine = pyttsx3.init()

    engine.setProperty('rate', 150)

    voices = engine.getProperty('voices')

    if lang == "en":
        engine.setProperty('voice', voices[0].id)  # English voice
    else:
        engine.setProperty('voice', voices[1].id)  # Other language voice

    engine.say(text)

    engine.runAndWait()

def speach_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("🎤 Listening...")

        audio = recognizer.listen(source)

    try:


        print(f"📝 You said: {text}")

        text = recognizer.recognize_google(audio, language="en-US")


    except sr.UnknownValueError:

        print("❌ Could not understand audio")

        return None

    except sr.RequestError as e:

        print(f"❌ Could not request results; {e}")

        return None

def translate_text(text, dest_lang="en"):
    translator = Translator()

    translation = translator.translate(text, dest=dest_lang)
    return translation.text

def display_language_options():
    print("🌐 Language Options:")
    print("1. English (en)")
    print("2. Hindi (hi)")
    print("3. Spanish (es)")
    print("4. French (fr)")
    print("5. German (de)")
    print("6. Italian (it)")
    print("7. Portuguese (pt)")
    print("8. Russian (ru)")
    print("9. Chinese (zh-CN)")
    print("10. Japanese (ja)")
    print("11. Korean (ko)")

    choice = input("Select a language by number (default is English): ")
    lang_map = {
        "1": "en",
        "2": "hi",
        "3": "es",
        "4": "fr",
        "5": "de",
        "6": "it",
        "7": "pt",
        "8": "ru",
        "9": "zh-CN",
        "10": "ja",
        "11": "ko"
    }
    return lang_map.get(choice, "en")

def main():
    target_lang = display_language_options()

    original_text = speach_to_text()

    if original_text:
        translated_text = translate_text(original_text, dest_lang=target_lang)

        print(f"🌍 Translated Text: {translated_text}")

        speak(translated_text, lang=target_lang)
        print("✅ Translation and speech synthesis complete!")

if __name__ == "__main__":
    main()