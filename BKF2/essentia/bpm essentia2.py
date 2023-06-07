import essentia
from essentia.standard import *

# Load the audio file
loader = MonoLoader(filename='/home/user/Music/early_years_terry.mp3') #returns a mono audio signal
audio = loader()

# Calculate the BPM
rhythm_extractor = RhythmExtractor2013()
bpm_tuple = rhythm_extractor(audio)
bpm = bpm_tuple[0]
print("Exact BPM:", bpm)
print("Rounded BPM ", round(bpm))
