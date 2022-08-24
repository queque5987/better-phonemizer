from lib2to3.pgen2 import token
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
from phonemizer import phonemize
import torch
import numpy as np

import compile_model

class phonemize_better:
    def __init__(self):
        self.tokenizer = self.load_tokenizer()
        print("loaded_tokenizer : {}".format(self.tokenizer.__class__.__name__))
        self.model = self.load_model()
        print("loaded_model : {}".format(self.model.__class__.__name__))

        print("loading checkpoint . . .")
        checkpoint = compile_model.load_model_split()
        self.model.load_state_dict(checkpoint)
        print("checkpoint loaded")

    def load_tokenizer(self):
        # model과 tokenizer pre-trained된 것 가져오기
        tokenizer = Wav2Vec2Tokenizer.from_pretrained("checkpoints/tokenizer")
        return tokenizer

    def load_model(self):
        # loading wav2vec2 model with no empty binary checkpoint file
        model = Wav2Vec2ForCTC.from_pretrained("checkpoints/model", ignore_mismatched_sizes = True)
        return model

    def speak_to_phoneme(self, audio, is_stress=False):
        tokenizer = self.tokenizer
        model = self.model
        assert type(audio) == np.ndarray
        # 유저 발화 파일 tokenizer에 넣기
        input_values = tokenizer(audio, return_tensors = "pt").input_values

        # 모델을 통해 logit값 출력(non_normalized)
        logits = model(input_values).logits

        # argmax를 통해 가장 가능성 높은 logits 들을 예측 logits으로
        prediction = torch.argmax(logits, dim = -1)

        # decoeding해서 text로 변환
        transcription = tokenizer.batch_decode(prediction)[0]

        print(transcription)
        print(phoneme)

        phoneme = self.text_to_phoneme(transcription, is_stress)
        return transcription, phoneme

    # text -> 음소
    def text_to_phoneme(self, transcription, is_stress=False):
        assert type(transcription) == str
        # 라이브러리를 활용해서 phoneme 변환
        phoneme = phonemize(transcription, with_stress=is_stress).rstrip()
        return phoneme

# if __name__ == "__main__":
#     # model = load_model()
#     print("loaded_model : {}".format(model.__class__.__name__))
#     checkpoint = compile_model.load_model_split()
#     model.load_state_dict(checkpoint)
#     print("state_loaded to {}".format(model.__class__.__name__))
#     tknzr = load_tokenizer()
    # sr, audio = wavfile.read("example.wav")
    # t, p = speak_to_phoneme(audio, tknzr, model)