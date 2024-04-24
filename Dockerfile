FROM python:3.11.4

COPY . /opt/
RUN pip install -r /opt/requirements.txt

RUN apt-get update && apt-get -y install vim

RUN echo "[i] Successful copy of the directory"
RUN echo "[i] Successful requirements installation"

# CMD ["python3", "pipelines/reddit_pipeline.py"]