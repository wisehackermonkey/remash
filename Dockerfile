FROM balenalib/raspberry-pi-debian-python:latest
WORKDIR /code
COPY requirements.txt ./
# RUN sudo apt install uwsgi-plugin-python3
RUN pip install --no-cache-dir -r ./requirements.txt
COPY . .

EXPOSE 8080
CMD [ "python", "./main.py" ]
