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
    return FileResponse("index.html")

@app.get('/inference')
async def inference(userinput: SpeakerInput):
    """
    @request
        transcription {str}
            text converting to phoneme
    @response
        phonemes {str}
            converted/phonemized text
    """

    userinput = userinput.dict()
    transcription = userinput["transcription"]
    phoneme = text_to_phoneme(transcription)
    phoneme = jsonable_encoder(phoneme)
    return JSONResponse(phoneme)