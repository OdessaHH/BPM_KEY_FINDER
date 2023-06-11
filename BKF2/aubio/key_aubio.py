import aubio

def estimate_key(audio_file):
    # Create aubio pitch object
    samplerate, win_s, hop_s = 44100, 2048, 512
    pitch_o = aubio.pitch("yin", win_s, hop_s, samplerate)

    # Open audio file
    audio = aubio.source(audio_file, samplerate, hop_s)
    total_frames = 0

    # Read audio frames and estimate pitch
    pitches = []
    while True:
        samples, read = audio()
        pitch = pitch_o(samples)[0]
        pitches.append(pitch)
        total_frames += read
        if read < hop_s:
            break

    # Estimate key from pitches
    pitch_mean = sum(pitches) / len(pitches)

    # Convert pitch to key index
    key_index = int((pitch_mean + 3) % 12)

    # Define a dictionary mapping key indices to key names
    key_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    # Get the estimated key name
    estimated_key = key_names[key_index]

    return estimated_key

# Example usage
audio_file = '/home/user/Music/early_years_terry.wav'
estimated_key = estimate_key(audio_file)
print(f"Estimated key: {estimated_key}")
