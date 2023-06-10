import essentia.standard as es

def estimate_key(audio_path):
    # Load audio using Essentia's MonoLoader
    loader = es.MonoLoader(filename=audio_path)
    audio = loader()

    # Extract key-related features using Essentia's KeyExtractor
    key_extractor = es.KeyExtractor()
    key, scale, key_strength = key_extractor(audio)

    return key, scale, key_strength

# Example usage
audio_path = '/home/user/Music/early_years_terry.mp3'
key, scale, key_strength = estimate_key(audio_path)

# Convert key strength to percentage and round to two decimal places
key_strength_percent = key_strength * 100
key_strength_rounded = round(key_strength_percent, 2)

# Print the estimated key, scale, and key strength
print("Estimated Key:", key)
if scale == 'major':
    print(f"Estimated Scale: # ({scale})")
else:
    print(f"Estimated Scale: b ({scale})")
print("Key Strength (%):", key_strength_rounded)

