FROM python:3.12

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./src /app/src

CMD ["fastapi", "run", "src/main.py", "--port", "8000", "--proxy-headers"]
