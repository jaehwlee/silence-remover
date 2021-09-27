from utils import remove_silence
from utils import load_audio


if __name__ == "__main__":
    PATH = '/some/where/file.wav'
    audio = load_audio(PATH)
    trimmed_audio = remove_silence(audio)
