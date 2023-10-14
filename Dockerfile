# Declare Python Version (Base Image) (Lightweight OS)
FROM --platform=linux/amd64 python:3.12

# Copy the code
COPY ./ /

# Declare ENV variable (not viable in company production code)
ENV DATABASE_URL=postgres://Auryx:1tZ4FmfKhzpg@ep-delicate-rain-59449480.us-west-2.aws.neon.tech/Movie_Tracker_v2

# Run installation for dependencies
RUN pip install -r dependencies.txt --verbose

# Run the App
CMD gunicorn -b 0.0.0.0:$PORT movieTracker.wsgi 

## Below are previous attempts at writing the Dockerfile

# # Making a working copy of the dependencies file
# COPY dependencies.txt dependencies.txt

# # Installing said dependencies
# RUN pip install -r dependencies.txt

# # Copying source code into the container (copying from this folder TO this folder)
# COPY . .

# # port declaration
EXPOSE 8000

# provide container default execution
# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]