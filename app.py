from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse, FileResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from utils import text_to_phoneme

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
    return FileResponse("a0.html")

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
    phoneme = text_to_phoneme(transcription)
    print("sending response: {}".format(phoneme))
    phoneme = jsonable_encoder(phoneme)
    return JSONResponse(phoneme)

@app.post('/test')
async def test(userinput: SpeakerInput):
    """
    @request
        transcription {str}
            text converting to phoneme
    @response
        phonemes {str}
            converted/phonemized text
    """
    print("service requested.")
    print(userinput.json())
    # phoneme = jsonable_encoder(phoneme)
    return JSONResponse(userinput)