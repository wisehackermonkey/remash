FROM python:3.8.6-alpine3.12
WORKDIR /code
COPY requirements.txt ./
# RUN sudo apt install uwsgi-plugin-python3
RUN pip install --no-cache-dir -r ./requirements.txt
COPY . .

EXPOSE 8080
CMD [ "python", "./main.py" ]
