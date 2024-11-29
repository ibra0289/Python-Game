FROM python:3.9-slim

WORKDIR /app

COPY Ibra0289_Assignment4.py ./game.py

CMD ["python", "game.py"]


