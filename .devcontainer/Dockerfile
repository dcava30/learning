FROM python:3.12

WORKDIR /learning

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /learning

EXPOSE 8501

CMD ["streamlit", "run", "curconvert.py"]

