FROM python:3

RUN  apt-get update  -y

RUN apt-get install -y software-properties-common \
    && add-apt-repository ppa:openjdk-r/ppa \
    && apt install -y openjdk-11-jdk openjdk-11-source \
    && rm -rf /var/lib/apt/lists/*

# java
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV INSIDE_DOCKER "True"

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -e .

CMD [ "task2", "word-counter" ]