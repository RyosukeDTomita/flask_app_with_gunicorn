FROM python:3.10
WORKDIR /usr/local/app
ENV FLASK_APP=app

RUN <<EOF
mkdir /usr/local/app
pip install flask
pip install gunicorn
EOF

COPY . .
EXPOSE 8000
