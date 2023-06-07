from music21 import *

def calculate_bpm(file_path):
    # Load the MIDI file
    midi_stream = converter.parse(file_path)
    
    # Estimate the BPM using the first part of the stream (assuming a single tempo for simplicity)
    first_part = midi_stream.parts[0]
    bpm_estimate = first_part.getElementsByClass('MetronomeMark')[0].getQuarterBPM()
    
    return bpm_estimate

# Specify the path to your MIDI file
midi_file_path = 'path_to_your_midi_file.mid'

# Calculate the BPM
bpm = calculate_bpm(midi_file_path)
print("Estimated BPM:", bpm)
