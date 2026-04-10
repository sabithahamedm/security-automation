#use official python image
FROM python:3.11-slim

#Set Working Directory
WORKDIR /app

#Copy the project file
COPY . .

#Install dependencies
RUN pip install --no-cache-dir requests

#Run the app
CMD ["python","main.py"]