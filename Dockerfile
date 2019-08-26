FROM python:latest
COPY . /usr/src/app
EXPOSE 8007:80
CMD ["python","api.py"]