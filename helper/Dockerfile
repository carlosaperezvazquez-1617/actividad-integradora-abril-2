FROM python:3.9-slim
WORKDIR /helper
RUN pip install flask
COPY status.py .
EXPOSE 5001
CMD ["python", "status.py"]