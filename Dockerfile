FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Tumia timeout ndefu na uhakikishe hakuna cache chafu inayobaki
RUN pip install --no-cache-dir --default-timeout=1000 flask scikit-learn pandas numpy waitress

COPY model.bin predict.py ./

EXPOSE 9696
CMD ["waitress-serve", "--host=0.0.0.0", "--port=9696", "predict:app"]