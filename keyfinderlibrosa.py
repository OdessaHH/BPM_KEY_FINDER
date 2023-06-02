import librosa
import numpy as np

def find_key(filepath):
    # Load the audio file
    audio, sr = librosa.load(filepath)

    # Convert the audio to mono if it's stereo
    if audio.ndim > 1:
        audio = librosa.to_mono(audio)

    # Extract the chromagram feature
    chromagram = librosa.feature.chroma_stft(y=audio, sr=sr)

    # Compute the average energy for each pitch class
    pitch_class_energy = np.mean(chromagram, axis=1)

    # Find the key with the maximum energy
    key_index = np.argmax(pitch_class_energy)

    # Map the key index to the corresponding key
    keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    key = keys[key_index]

    return key

# Usage example
filepath = '/home/user/Music/keybpm.wav'
key = find_key(filepath)
print("The key of the track is:", key)
