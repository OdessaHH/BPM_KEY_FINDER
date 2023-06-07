import essentia
from essentia.standard import *

# Load the audio file
loader = MonoLoader(filename='/home/user/Music/keybpm.wav')
audio = loader()

# Calculate the rhythmic features
rhythm_extractor = RhythmExtractor2013()
bpm, beats, confidence, loudness, descriptors = rhythm_extractor(audio)

# Access the beat positions
print("Beat Positions:", beats)

# Access the confidence values for each beat
print("Beat Confidence:", confidence)

# Access the loudness values for each beat
print("Beat Loudness:", loudness)

# Access the descriptors for each beat
print("Beat Descriptors:", descriptors)
