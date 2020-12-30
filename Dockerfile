FROM python:3.8.7-slim

ARG APP_PATH=/home/app
RUN mkdir -p ${APP_PATH}
COPY . ${APP_PATH}
WORKDIR ${APP_PATH}

RUN pip install pipenv
RUN pipenv install --deploy --system --ignore-pipfile
RUN python webserver.py &
EXPOSE 8085
CMD ["python", "main.py"]
