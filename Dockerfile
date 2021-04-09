FROM python:3.9.1-slim

ARG APP_PATH=/home/app
RUN mkdir -p ${APP_PATH}
COPY . ${APP_PATH}
WORKDIR ${APP_PATH}

RUN pip install pipenv
RUN pipenv install --deploy --system --ignore-pipfile
EXPOSE 8085
CMD ["python", "main.py"]
