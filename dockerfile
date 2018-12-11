# base image
FROM python:3.6.5-alpine

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

# set working directory
WORKDIR ./

# add and install requirements
COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

# add entrypoint.sh
COPY ./entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

# add app
COPY . /.

# run server
CMD ["./entrypoint.sh"]