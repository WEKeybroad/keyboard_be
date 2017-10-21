FROM python:2.7
MAINTAINER key

ENV DEPLOY_PATH /key 

RUN mkdir -p $DEPLOY_PATH 
WORKDIR $DEPLOY_PATH 

Add requirements.txt requirements.txt 
RUN pip install --index-url http://pypi.doubanio.com/simple/ -r requirements.txt --trusted-host=pypi.doubanio.com

Add . . 
