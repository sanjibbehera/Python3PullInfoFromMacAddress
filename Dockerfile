FROM python:3.6-alpine
RUN pip install requests
COPY . /opt/
WORKDIR /opt
CMD ["python","server.py","-a","(mac-addr) ","-t","(api-token)"]