import madmom
from collections.abc import MutableSequence

def calculate_bpm(file_path):
    # Load the audio file
    audio, sample_rate = madmom.audio.signal.load_audio_file(file_path)

    # Beat tracking
    proc = madmom.features.beats.RNNBeatProcessor()
    act = proc(audio)

    # Calculate the BPM
    bpm_processor = madmom.features.tempo.TempoEstimationProcessor(fps=100)
    bpm_values = bpm_processor(act)

    if bpm_values:
        bpm = bpm_values[0]
    else:
        bpm = 0

    return bpm

def main():
    file_path = '/home/user/Music/keybpm.wav'  # Replace with the path to your audio file

    print("Welcome to the MaDMoM BPM Counter!")
    print("Analyzing the track...")

    try:
        bpm = calculate_bpm(file_path)
        print("BPM:", bpm)

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == '__main__':
    main()
