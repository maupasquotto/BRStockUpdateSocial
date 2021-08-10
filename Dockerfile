FROM python:3.9.6-slim

# Copy necessary files
ADD brstockupdatePost.py .
ADD requirements.txt .
ADD .env .
ADD env env

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "brstockupdatePost.py" ]