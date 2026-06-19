FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
RUN adduser --disabled-password --gecos "" appuser
COPY pyproject.toml README.md requirements.lock ./
COPY src ./src
COPY tests ./tests
COPY config ./config
COPY alembic.ini ./
COPY alembic ./alembic
RUN pip install --no-cache-dir .[dev]
USER appuser
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/v1/health').read()"
CMD ["uvicorn", "quectosoft_hr.api:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
