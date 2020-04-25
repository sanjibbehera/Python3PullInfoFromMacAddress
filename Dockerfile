FROM python:3.6-alpine
RUN pip install requests
COPY . /opt/
WORKDIR /opt
RUN chmod +x /opt/entrypoint.sh
ENTRYPOINT ["sh", "/opt/entrypoint.sh"]