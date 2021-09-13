FROM python:3.7-stretch
COPY . /app
WORKDIR /app
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
RUN pip install -r requirements.txt
EXPOSE 5000
#ARG request_domain=http://todoapp:5000
#ENV request_domain=$request_domain
ENTRYPOINT [ "python" ]
CMD [ "taskapi.py" ]
