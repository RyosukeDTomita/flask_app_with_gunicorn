FROM python:3.10
WORKDIR /usr/src/app
ENV FLASK_APP=app

RUN <<EOF
mkdir /usr/src/app
pip install flask
EOF

COPY app.py ./
EXPOSE 5000
