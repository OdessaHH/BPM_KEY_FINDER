import librosa
import numpy as np

def extract_features(audio_file):
    # Load audio file
    audio, sr = librosa.load(audio_file)

    # Extract chromagram feature
    chromagram = librosa.feature.chroma_stft(y=audio, sr=sr)

    # Calculate the mean of the chromagram
    chroma_mean = np.mean(chromagram, axis=1)

    return chroma_mean

def estimate_key(audio_file):
    # Extract features from the audio file
    features = extract_features(audio_file)

    # Define a dictionary mapping key indices to key names
    key_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    # Find the index of the maximum value in the feature vector
    estimated_key_index = np.argmax(features)

    # Map the index to the corresponding key name
    estimated_key = key_names[estimated_key_index]

    return estimated_key

# Example usage
audio_file = '/home/user/Music/keybpm.wav'
estimated_key = estimate_key(audio_file)
print(f"Estimated key: {estimated_key}")
