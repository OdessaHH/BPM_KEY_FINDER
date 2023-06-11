import essentia.standard as es

def calculate_bpm(audio_path):
    # Load audio file
    loader = es.MonoLoader(filename=audio_path)
    audio = loader()

    # Calculate beats using BeatTrackerDegara algorithm
    beat_tracker = es.BeatTrackerDegara()
    beats = beat_tracker(audio)

    # Calculate the average inter-beat intervals manually
    intervals = []
    for i in range(len(beats) - 1):
        interval = beats[i + 1] - beats[i]
        intervals.append(interval)

    # Calculate the mean interval to estimate the BPM
    bpm = 60.0 / (sum(intervals) / len(intervals))

    return bpm

# Example usage
audio_file = "/home/user/Music/early_years_terry.mp3"
bpm = calculate_bpm(audio_file)
print("Exact BPM:", bpm)
print("Rounded BPM:", round(bpm))
