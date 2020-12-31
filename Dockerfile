From python:3.8
WorkDir /app
RUN pip install requests
RUN pip install PyBluez
RUN pip install pymongo
COPY ./src /app
CMD python /app/app.py