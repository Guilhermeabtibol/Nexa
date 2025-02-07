import speech_recognition as sr
import pyttsx3

# Inicializa o reconhecedor de voz
recognizer = sr.Recognizer()

# Inicializa o sintetizador de voz
engine = pyttsx3.init()

# Configurações de voz (opcional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Escolhe a voz (0 para masculino, 1 para feminino)
engine.setProperty('rate', 150)  # Velocidade da fala

def falar(texto):
    """Faz o bot falar um texto."""
    print(f"Bot: {texto}")
    engine.say(texto)
    engine.runAndWait()

def escutar():
    """Captura a fala do usuário e converte para texto."""
    with sr.Microphone() as source:
        print("Ouvindo...")
        recognizer.adjust_for_ambient_noise(source)  # Ajusta para o ruído ambiente
        audio = recognizer.listen(source)

        try:
            texto = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {texto}")
            return texto.lower()
        except sr.UnknownValueError:
            return "Desculpe, não entendi."
        except sr.RequestError:
            return "Erro ao conectar ao serviço de reconhecimento de voz."

def main():
    falar("Olá! Eu sou um bot de voz. Como posso ajudar você hoje?")
    
    while True:
        mensagem_usuario = escutar()
        print(f"Você: {mensagem_usuario}")

        if "tchau" in mensagem_usuario:
            falar("Até logo! Foi um prazer ajudar.")
            break

        # Respostas pré-definidas
        if "oi" in mensagem_usuario:
            falar("Olá! Como posso ajudar você hoje?")
        elif "como você está" in mensagem_usuario:
            falar("Estou funcionando perfeitamente, obrigado por perguntar!")
        elif "qual é o seu nome" in mensagem_usuario:
            falar("Eu sou um bot simples criado em Python.")
        elif "o que você faz" in mensagem_usuario:
            falar("Eu respondo perguntas com base nas minhas respostas pré-definidas.")
        else:
            falar("Desculpe, não entendi. Pode repetir?")

if __name__ == "__main__":
    main()