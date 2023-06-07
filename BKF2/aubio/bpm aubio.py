import aubio
from aubio import source, tempo

def calculate_bpm(audio_file):
    win_s = 512                 # Window size for analysis
    hop_s = win_s // 2          # Hop size (overlap)

    samplerate = 0              # Placeholder for the actual samplerate
    s = source(audio_file, samplerate, hop_s)
    samplerate = s.samplerate

    o = tempo("default", win_s, hop_s, samplerate)

    # List to store the detected beats
    beats = []

    # Process the audio file until all frames have been read
    while True:
        samples, read = s()
        is_beat = o(samples)
        if is_beat:
            this_beat = o.get_last_s()
            beats.append(this_beat)
        if read < hop_s:
            break

    # Calculate the BPM from the detected beats
    bpm = o.get_bpm()
    return bpm

# Provide the path to your audio file
audio_file_path = "/home/user/Music/early_years_terry.wav"
bpm = calculate_bpm(audio_file_path)
print("Exact BPM:", bpm)
print("Rounded BPM:", round(bpm))
