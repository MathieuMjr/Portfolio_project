FROM python



WORKDIR /portfolio
COPY ../../app ./
COPY ../..seed ./
COPY ../../config.py ./
COPY ../../requirements.txt ./
COPY ../../run.py ./
COPY ../../.env ./

RUN python3 -m venv venv
RUN source venv/bin/activate
RUN pip-install -r requirements.txt

RUN python3 -m seed.seed-db

CMD [python3, run.py]