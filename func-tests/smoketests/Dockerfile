FROM debian:buster-backports

RUN apt-get update \
    && apt-get install -y curl \
    && apt-get install -y python3-requests \
    && apt-get clean -y

RUN ln -s /usr/bin/yarnpkg /usr/bin/yarn

RUN mkdir /opt/test
COPY . /opt/test
WORKDIR /opt/test

