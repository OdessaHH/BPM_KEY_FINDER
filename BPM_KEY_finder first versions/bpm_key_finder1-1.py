import tkinter as tk
import tkinter.filedialog as filedialog
import numpy as np
import librosa
import madmom

def estimate_bpm(audio_file):
    # Load Audio
    audio_data, sample_rate = librosa.load(audio_file, sr=None)

    # Estimate BPM
    tempo, beat_frames = librosa.beat.beat_track(y=audio_data, sr=sample_rate)
    estimated_bpm.set(tempo)

def estimate_key(audio_file):
    # Estimate Key
    key_detector = madmom.features.key.CNNKeyRecognitionProcessor()
    key_estimation = key_detector(audio_file)
    key = key_estimation[0]
    max_index = np.argmax(key)
    
    # Mapping of index to musical keys
    musical_keys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    
    # Get the corresponding musical key
    estimated_key_str = musical_keys[max_index]
    estimated_key.set(estimated_key_str)

def choose_file():
    # Open file dialog to choose audio file
    file_path = filedialog.askopenfilename(initialdir="/home/user/Music", title="Select Audio File", filetypes=[("Audio Files", "*.*")])
    if file_path:
        # Call estimation functions with the selected file path
        estimate_bpm(file_path)
        estimate_key(file_path)

# Create the main window
window = tk.Tk()
window.title("Audio Analysis")
window.geometry("400x200")  # Set window size (width x height)

# Create labels for BPM and Key estimation
bpm_label = tk.Label(window, text="Estimated BPM:", font=("Arial", 14))  # Customize label font and size
bpm_label.pack()
estimated_bpm = tk.StringVar()
bpm_value = tk.Label(window, textvariable=estimated_bpm, font=("Arial", 16, "bold"))  # Customize value font, size, and style
bpm_value.pack()

key_label = tk.Label(window, text="Estimated Key:", font=("Arial", 14))
key_label.pack()
estimated_key = tk.StringVar()
key_value = tk.Label(window, textvariable=estimated_key, font=("Arial", 16, "bold"))
key_value.pack()

# Create button to choose file
file_button = tk.Button(window, text="Choose File", command=choose_file, font=("Arial", 12))  # Customize button font and size
file_button.pack()

# Start the GUI main loop
window.mainloop()
