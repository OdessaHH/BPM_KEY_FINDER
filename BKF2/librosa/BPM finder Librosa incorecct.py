import librosa

def calculate_bpm(audio_file):
    # Load the audio file
    y, sr = librosa.load(audio_file)

    # Estimate the tempo
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

    return tempo


# Provide the path to your audio file
audio_file = '/home/user/Music/keybpm.wav'

# Calculate the BPM
bpm = calculate_bpm(audio_file)

# Print the result
print(f"The estimated BPM is: {bpm}")
