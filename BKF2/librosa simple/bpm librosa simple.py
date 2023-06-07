import librosa

# Load the audio file
audio_file = '/home/user/Music/early_years_terry.mp3'
y, sr = librosa.load(audio_file)

# Calculate the tempo (BPM)
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

print("Exact BPM:", tempo)
print("Rounded BPM:", round(tempo))


#is not precise enough, but easy to use
