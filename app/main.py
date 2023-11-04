import joblib
import requests
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
# from predict import predict_sentiment  # Local
from tensorflow import keras

from app.predict import predict_sentiment  # Docker

tokenizer = joblib.load(f'model/tokenizer.pkl')
# tokenizer = joblib.load(r'C:\Users\User\Desktop\AI\Project\Sentiment\model\tokenizer.pkl') #local
model = keras.models.load_model(f"model/lstm_model.pkl") 
# model = keras.models.load_model(r"C:\Users\User\Desktop\AI\Project\Sentiment\model\lstm_model.pkl") 

end_cleantext = 'http://172.17.0.2:80/api/cleantext' #Docker
# end_cleantext = 'http://localhost:8080/api/cleantext' #Local


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/sentiment")
async def read_str(request:Request):
    item = await request.json()
    text = requests.get(end_cleantext,json=item)
    respond = predict_sentiment(model,tokenizer,text.json()['text'])
    return respond

# item = {"text":"tock love @ppp"}
# text = requests.get(end_cleantext,json=item)
# print (text.json()['text'])