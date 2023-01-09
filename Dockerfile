FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1\
    PYTHONUNBUFFERED=1\
    POETRY_VERSION=1.1.15\
    PATH="${PATH}:/usr/local/bin/python" \
    PATH="${PATH}:/root/.poetry/bin"

WORKDIR /app
COPY . .

ENV PATH="${PATH}:/usr/local/bin/python" \
    PATH="${PATH}:/root/.poetry/bin"

RUN pip install --upgrade pip \
    && pip install "poetry==$POETRY_VERSION" \
    && poetry config virtualenvs.create false \
    && poetry export --without-hashes -f requirements.txt > requirements.txt \
    && python -m pip install -r requirements.txt --no-cache

EXPOSE 5000

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
