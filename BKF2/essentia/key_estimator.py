import essentia.standard as es

def key_estimate(audio_path):
    # Load audio using Essentia's MonoLoader
    loader = es.MonoLoader(filename=audio_path)
    audio = loader()

    # Extract key-related features using Essentia's KeyExtractor
    key_extractor = es.KeyExtractor()
    key, scale, key_strength = key_extractor(audio)

    return key, scale, key_strength
