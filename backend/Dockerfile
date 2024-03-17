FROM python:alpine3.7 
COPY . /app
WORKDIR /app
RUN ls
RUN pip install -r requirements.txt 
EXPOSE 5001 
ENTRYPOINT [ "python" ] 
CMD [ "src/main.py" ] 
