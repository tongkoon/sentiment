from keras.preprocessing.sequence import pad_sequences

text = "hello tock hate sick bad"
def predict_sentiment(model,tokenizer,text):
    vector=pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=100)
    score=model.predict(vector)

    if score[0]>=0.5:
        result = "Positive"
    else:
        result = "Negative"

    return {"respond":result}

# data = predict_sentiment(text)
# print (data)