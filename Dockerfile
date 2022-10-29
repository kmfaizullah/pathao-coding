FROM python:3.8-slim-buster
RUN apt update && apt install -y nginx gettext
# creating working directory
RUN mkdir /app
# set work directory
WORKDIR /app

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN rm /etc/nginx/sites-available/default
COPY scripts/nginx/default.conf /etc/nginx/sites-available/default

COPY scripts/entrypoint.sh .
RUN chmod +x ./entrypoint.sh

COPY . .

EXPOSE 80
# ENTRYPOINT ["./entrypoint.sh"]
CMD ["bash", "-c", "gunicorn --workers 2 --preload --bind 0.0.0.0:8000 config.wsgi:application & nginx -g 'daemon off;'"]