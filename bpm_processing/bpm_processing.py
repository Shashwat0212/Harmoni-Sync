import librosa


def calculate_bpm(filePath):
    filePath = filePath.replace("\\", "\\")
    audio_file = librosa.load(filePath)

    y, sr = audio_file

    temp = librosa.beat.tempo(y=y, sr=sr)

    return round(temp[0])
