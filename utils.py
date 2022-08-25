# from phonemizer import phonemize
import espeak_phonemizer

def text_to_phoneme(transcription, is_stress=False):
    assert type(transcription) == str
    pmzr = espeak_phonemizer.phonemizer()
    phoneme = pmzr.phonemize(transcription).rstrip()
    return phoneme