FROM python:3.6.8-alpine3.6
WORKDIR /code
COPY requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt
COPY . .

EXPOSE 8080
CMD [ "python", "./main.py" ]