
import numpy as np

import alsaaudio


# Set the compressor threshold and ratio
threshold = 0.1
ratio = 4

# Open the PCM audio stream
pcm = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)

# Set the sample rate, number of channels, and sample format
pcm.channels(2)
pcm.rate(44100)
pcm.format(alsaaudio.PCM_FORMAT_S16_LE)

# Set the period size and number of periods
periodsize = 1024
pcm.periodsize(periodsize)


numperiods = 4
pcm.periods(numperiods)

while True:
    # Read the audio data from the stream
    length, data = pcm.read()

    if length:
        # Convert the audio data to a NumPy array
        audio = np.frombuffer(data, dtype='int16')

        # Calculate the root-mean-square (RMS) of the audio signal
        rms = np.sqrt(np.mean(audio**2))

        # Define the gain reduction function
        def gain_reduction(x):
            if x > threshold:
                return threshold + (x - threshold) / ratio
            else:
                return x

        # Apply the gain reduction function to the audio signal
        audio_comp = np.array([gain_reduction(x) for x in audio])

        # Convert the compressed audio data back to bytes
        data_comp = audio_comp.astype('int16').tobytes()

        # Write the compressed audio data back to the stream
        pcm.write(data_comp)
