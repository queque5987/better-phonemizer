Better-API (phonemizer)
=============

### Better-API (phonemizer)   
Better-phonemizer convert text into phonemes
    
## Available on
https://better-phonemizer.herokuapp.com/
## to Inference, send request on
https://better-phonemizer.herokuapp.com/inference/
### Request {JSON}
    transcription {str}   
**receives {str} transcription to transform*   
### Response {JSON}
    phonemes {str}         
**return transcription that is transformed into phonemes*    

* * *
# used libraries
## English-to-ipa
https://github.com/vpnry/english-to-ipa

## FastAPI   
developed with FastAPI   
source : https://fastapi.tiangolo.com/   

## Heroku
For deployment, I used Heroku
https://dashboard.heroku.com/

## requirements.txt
### For deployment
    fastapi
    pydantic
    uvicorn
    favicon
    gunicorn
### For Voice clonning   
    numpy
    eng_to_ipa

-----
Better-API (phonemizer)
=============

### Better-API (phonemizer)   
Better-phonemizer는 알파벳으로 작성된 문장을 음소로 변환시켜 줍니다.
    
## Available on
https://better-phonemizer.herokuapp.com/
## to Inference, send request on
https://better-phonemizer.herokuapp.com/inference/
### Request {JSON}
    transcription {str}   
**{str}타입의 transcription를 전달받습니다.*   
### Response {JSON}
    phonemes {str}         
**{str}타입의 음소로 변환된 transcription을 반환합니다.*    

* * *
# used libraries
## English-to-ipa
https://github.com/vpnry/english-to-ipa

## FastAPI   
FastAPI를 사용하여 개발되었습니다.   
source : https://fastapi.tiangolo.com/   

## Heroku
Heroku를 사용하여 배포하였습니다.
https://dashboard.heroku.com/

## requirements.txt
### For deployment
    fastapi
    pydantic
    uvicorn
    favicon
    gunicorn
### For Voice clonning   
    numpy
    eng_to_ipa

## 사용예시(Examples)   
### input
    Jack and Jill ran up the hill.   
### output
    ʤæk ənd ʤɪl ræn əp ðə hɪl.   

### on Python
```python
import requests
import json

url = "https://better-phonemizer.herokuapp.com/inference"

def get_embed():
    text = "Jack and Jill run up the hill." # input
    transcription_json = json.dumps({
        "transcription": text
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=transcription_json)
    res = eval(response.json())
    print(res['transcription']) # output
```

### on JavaScript
```javascript
var obj = new Object();
obj.transcription = text; // text : input
var jsonString = JSON.stringify(obj)
var res = fetch('https://better-phonemizer.herokuapp.com/inference', {
  method: 'POST',
  headers: {
  'Content-Type': 'application/json',
  },
  body: jsonString
}).then((response) => response.json()
).then(function(data){
  var res = JSON.parse(data)
  console.log(res.transcription) // res.transcription : output
})
```
