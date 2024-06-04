import speech_recognition as sr
import pyttsx3
import spacy

# Inicializar o recognizer e o engine de síntese de voz
recognizer = sr.Recognizer()
engine = pyttsx3.init()
nlp = spacy.load("pt_core_news_sm")

# Função para converter texto em fala


def speak(text):
    engine.say(text)
    engine.runAndWait()

# Função para reconhecer fala


def recognize_speech_from_mic():
    with sr.Microphone() as source:
        print("Ajustando o microfone para eliminar o ruído...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Fale algo!")
        audio = recognizer.listen(source)

        try:
            print("Reconhecendo...")
            text = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {text}")
            return text
        except sr.UnknownValueError:
            print("Desculpe, não entendi o que você disse.")
            return ""
        except sr.RequestError:
            print("Erro de conexão com o serviço de reconhecimento de fala.")
            return ""

# Função para processar texto com spaCy


def process_text_with_spacy(text):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    tokens_filtrados = [token.text for token in doc if not token.is_stop]
    lematizados = [token.lemma_ for token in doc]
    return tokens, tokens_filtrados, lematizados


# Loop principal
while True:
    print("Diga 'sair' para encerrar.")
    comando = recognize_speech_from_mic()

    if "sair" in comando.lower():
        speak("Encerrando o programa. Até logo!")
        break
    else:
        # Processar o comando com spaCy
        tokens, tokens_filtrados, lematizados = process_text_with_spacy(
            comando)
        response = f"Tokens: {tokens}\nTokens filtrados: {
            tokens_filtrados}\nLematizados: {lematizados}"
        print(response)
        speak(response)
