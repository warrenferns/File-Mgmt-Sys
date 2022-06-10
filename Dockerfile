FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN apt-get update && \
      apt-get -y install sudo
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["main.py"]