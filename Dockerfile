FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt ./
RUN apt-get update && apt-get install -y build-essential
RUN pip install --user -r requirements.txt
COPY . .

FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /app /app
COPY --from=builder /root/.local /root/.local

ENV PATH=/root/.local/bin:$PATH
EXPOSE 5000
CMD ["python", "app.py"]

