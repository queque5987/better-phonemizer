from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import numpy as np

import phonemize

app = FastAPI()

class SpeakerInput(BaseModel):
    wav: list

@app.get('/')
def index():
    return "This is the phonemizer part of better-project API."

@app.get('/inference/')
async def inference(userinput: SpeakerInput):
    """
    @request
        user voice sample {list}
            {array} wav, {int} sample_rate loaded by librosa
    @response
        user voice embedding {list}
            {ndarray} embedding converted into {list} so that it could be sent as a request;

    **This method returns user utterance embedding inferenced by Speaker Encoder**
    """
    userinput = userinput.dict()
    wav = userinput["wav"]
    wav = np.array(wav)
    phonemize.speak_to_phoneme(wav)
    wav = jsonable_encoder(wav.tolist())
    return JSONResponse(wav)