FROM debian:11
RUN apt update # ...update+upgrade
RUN apt-get install -y python3-pip
RUN pip install fastapi uvicorn
WORKDIR /srv # il faut bien sur que ce dossier existe ...
COPY app1.py .
CMD uvicorn app1:app --host 0.0.0.0
