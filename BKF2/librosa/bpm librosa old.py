import librosa

def estimate_bpm(audio_file):
    # Load Audio
    audio_data, sample_rate = librosa.load(audio_file, sr=None)

    # Estimate BPM
    tempo, beat_frames = librosa.beat.beat_track(y=audio_data, sr=sample_rate)
    estimated_bpm = round(tempo)  # Round the BPM value

    return estimated_bpm

audio_file = '/home/user/Music/keybpm.wav'

print(estimate_bpm(audio_file))

audio_file2 = '/home/user/Music/early_years_terry.mp3'

print(estimate_bpm(audio_file2))

