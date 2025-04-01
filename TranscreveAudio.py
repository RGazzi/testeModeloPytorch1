import speech_recognition as sr

class AudioTranscriber:
    def __init__(self, audio_path):
        self.audio_file_path = audio_path
        self.recognizer = sr.Recognizer()

    def transcribe_audio(self):
        """Transcreve o áudio e retorna o texto."""
        with sr.AudioFile(self.audio_file_path) as source:
            audio = self.recognizer.record(source)
            print("Lendo arquivo de áudio...")

        try:
            text = self.recognizer.recognize_google(audio, language='pt-BR')
            print(f"Texto Transcrito: {text}")
            return text
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio.")
            return "não entendi."
        except sr.RequestError:
            print("Erro na requisição ao serviço de reconhecimento de fala.")
            return "erro no reconhecimento."
