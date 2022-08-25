from phonemizer import phonemize

def text_to_phoneme(transcription, is_stress=False):
    assert type(transcription) == str
    phoneme = phonemize(transcription, with_stress=is_stress).rstrip()
    return phoneme