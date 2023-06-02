import numpy as np
print(np.__version__)  # Print the version of NumPy library

import librosa
import madmom

# Load Audio
audio_file = "/home/user/Music/early_years_terry.mp3"
audio_data, sample_rate = librosa.load(audio_file, sr=None)  # Load audio file and preserve the original sample rate

# Estimate BPM
tempo, beat_frames = librosa.beat.beat_track(y=audio_data, sr=sample_rate)  # Estimate the tempo (beats per minute) of the audio

print("Estimated BPM:", tempo)  # Print the estimated BPM

# Estimate Key
key_detector = madmom.features.key.CNNKeyRecognitionProcessor()  # Create a key detection object
key_estimation = key_detector(audio_file)  # Estimate the key of the audio
key = key_estimation[0]  # Get the estimated key
print("Estimated Key:", key)  # Print the estimated key

max_index = np.argmax(key)  # Find the index of the maximum value in the estimated key array

# Mapping of index to musical keys
musical_keys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Get the corresponding musical key
estimated_key_str = musical_keys[max_index]  # Map the index to the musical key
print("Estimated Key:", estimated_key_str)  # Print the estimated key in a readable format
