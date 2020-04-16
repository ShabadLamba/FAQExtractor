FROM ubuntu:18.04
LABEL maintainer="Shabad Lamba <shabad.l@imimobile.com>"

RUN apt-get update && apt-get install -y \
    python3 \
    python3-dev \
    python3-pip \
    nginx \
    git

RUN echo $(pwd)
#COPY . ./entity_tagging
RUN git clone https://github.com/ShabadLamba/FAQExtractor.git
WORKDIR ./FAQExtractor/Backend
ENV LANG C.UTF-8
RUN pip3 install -r requirements.txt

#RUN chmod +x app.py
#this is the command which will run the flask api to start the server
#CMD python3 app.py
CMD python3 QnAApi.py
