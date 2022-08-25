# from phonemizer import phonemize
# import espeak_phonemizer
import eng_to_ipa as ipa

# def text_to_phoneme(transcription, is_stress=False):
#     assert type(transcription) == str
#     pmzr = espeak_phonemizer.Phonemizer()
#     phoneme = pmzr.phonemize(transcription).rstrip()
#     return phoneme

def text_to_phoneme(transcription, text = "ABOUT YOUNG GIRLS THAT HAVE BEEN SPOILT FOR HOME BY GREAT ACQUAINTANCE THE MIRROR I THINK I WILL LOOK IT OUT FOR YOU SOME DAY OR OTHER BECAUSE I AM SURE IT WILL DO YOU GOOD CATHERINE SAID NO MORE AND WITH AN ENDEAVOUR TO DO RIGHT"):
    phoneme = ipa.convert(text)
    phoneme = phoneme.split("p15081553y*")
    return phoneme