import speech_recognition as speech
import webbrowser


core = speech.Recognizer()

dictCommands = {
    "Commands": ["YouTube", "ВК"],
    "StartWords": ["Открой"]
}


def engineSpeech():
    with speech.Microphone() as micro:
        print("Слушаю")
        audio = core.listen(micro)
    try:
        result = core.recognize_google(audio, language="ru-RU")
        response = analizeData(result)
        return response
    except speech.UnknownValueError:
        print("Не удалось распознать речь")
    except speech.RequestError as e:
        print(e)

def analizeData(response):
    formattedText = response.split(" ")
    if formattedText[0] in dictCommands["StartWords"]:
        startActivity(formattedText[1])
    else:
        print("dd")

def startActivity(activity):
    if activity == dictCommands["Commands"][0]:
        webbrowser.open_new_tab("https://www.youtube.com")
    elif activity == dictCommands["Commands"][1]:
        webbrowser.open_new_tab("https://vk.com/feed")
    else:
        return "Извините, но я не смогу выполнить"



while True:
    engineSpeech()