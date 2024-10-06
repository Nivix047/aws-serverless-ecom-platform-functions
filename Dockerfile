# Use the AWS Lambda Python 3.11 runtime as a base image
FROM public.ecr.aws/lambda/python:3.11

# Set the working directory inside the container
WORKDIR /var/task

# Copy the application code into the container
COPY app.py ./

# Copy the requirements.txt file and install the Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Set the CMD to point to your Lambda function handler
CMD ["app.lambda_handler"]
