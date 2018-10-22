# base image
FROM python:3.6.5-alpine

# set working directory
WORKDIR ./

# add and install requirements
COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

# add app
COPY . /.

# run server
CMD python3 manage.py run -h 0.0.0.0