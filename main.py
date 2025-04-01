from Resposta import RespostaUsuario
from TranscreveAudio import AudioTranscriber

# Pressione o botão verde para rodar o script
if __name__ == '__main__':
    audio_path = 'venv/audio_files/Audio_ola.wav'
    print("Iniciando o assistente com áudio capturado...")

    # Transcrever o áudio
    transcriber = AudioTranscriber(audio_path)
    comando = transcriber.transcribe_audio()

    # Criar instância do RespostaUsuario e processar o comando
    resposta_usuario = RespostaUsuario("Ricardo", comando)
    resposta_usuario.ProcessarComando()
