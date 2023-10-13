# Declare Python Version (Base Image) (Lightweight OS)
FROM python:3.8

# IDing the working directory path
WORKDIR /movies

# Making a working copy of the dependencies file
COPY dependencies.txt dependencies.txt

# Installing said dependencies
RUN pip install -r dependencies.txt

# Copying source code into the container (copying from this folder TO this folder)
COPY . .

# port declaration
EXPOSE 8000

# provide container default execution
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]