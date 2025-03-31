import speech_recognition as sr

class AudioTranscriber:
    def __init__(self, audio_file_path):
        self.audio_file_path = audio_file_path
        self.recognizer = sr.Recognizer()

    def transcribe_audio(self):
        #abrir arquivo
        with sr.AudioFile(self.audio_file_path) as source:
            audio = self.recognizer.record(source)
            print("ver função")

        try:
            #usando o Google Web Speech API para reconhecer o áudio
            text = self.recognizer.recognize_google(audio, language='pt-BR')
            print(f"Texto Transcrito: {text}")
        except sr.UnknownValueError:
            print("não foi possível ouvir o áudio")
        except sr.RequestError:
            print(f"erro na requisição ao serviço de reconhecimento de fala, {e}")

audio_path = 'venv/audio_files/Audio_ola.wav'


transcriber = AudioTranscriber(audio_path)
transcriber.transcribe_audio()
