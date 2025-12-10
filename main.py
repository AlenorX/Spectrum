import speech_recognition as speech


core = speech.Recognizer()

dictCommands = {
    "StartWord": ["спектрум", "spectrum"],
    "Commands": ["YouTube", "BK"]
}


def engineSpeech():
    with speech.Microphone() as micro:
        print("Слушаю")
        audio = core.listen(micro)
    try:
        result = core.recognize_google(audio, language="ru-RU")
        analizeData(result)
    except speech.UnknownValueError:
        print("Не удалось распознать речь")
    except speech.RequestError as e:
        print(e)

def analizeData(response):
    print(response)


    
        

while True:
    engineSpeech()