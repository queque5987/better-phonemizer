"""
    ***************************************************
    author: Park Young-woong
    e-mail: pyw5987@gmail.com
    github: https://github.com/queque5987/better-encoder
    ***************************************************
"""
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse, FileResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from utils import text_to_phoneme
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SpeakerInput(BaseModel):
    transcription: str

@app.get('/')
def index():
    return FileResponse("index.html")

@app.post('/inference')
def inference(userinput: SpeakerInput):
    """
    @request
        transcription {str}
            text converting to phoneme
    @response
        phonemes {str}
            converted/phonemized text
    """
    print("service requested.")
    userinput = userinput.dict()
    transcription = userinput["transcription"]
    print("inserted transcription: {}".format(transcription))
    phoneme = text_to_phoneme(transcription)[0]
    print("sending response: {}".format(phoneme))
    # phoneme = jsonable_encoder(phoneme)
    phoneme_json = json.dumps({
        "transcription": phoneme
    })
    return JSONResponse(phoneme_json)
