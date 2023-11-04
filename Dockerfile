# 
FROM python:3.9

# 
WORKDIR /Sentiment

# 
COPY ./requirements.txt /Sentiment/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /Sentiment/requirements.txt

# 
COPY ./app /Sentiment/app
COPY ./model /Sentiment/model

ENV PYTHONPATH "${PYTHONPATH}:/Sentiment"

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]