FROM python:3.9.1-slim

# ADD LOCALES
RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

ENV LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8
# END: ADD LOCALES

ARG APP_PATH=/home/app
RUN mkdir -p ${APP_PATH}
COPY . ${APP_PATH}
WORKDIR ${APP_PATH}

RUN pip install pipenv
RUN pipenv install --deploy --system --ignore-pipfile
EXPOSE 8085
CMD ["python", "main.py"]
