FROM python:3.11-bullseye

WORKDIR /app/
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["fastapi", "dev", "src/__init__.py"]
CMD ["--host", "0.0.0.0", "--port", "5000"]
