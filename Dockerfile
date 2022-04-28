FROM public.ecr.aws/lambda/python:3.6

# Copy function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

# Install the function's dependencies using file requirements.txt
# from your project folder.

COPY requirements.txt  .

ENV BASELINE_FILE s3://bucket/parquet-files-order_status/
ENV BUCKET_NAME practice
ENV FILE_PREFIX retail_db/orders/part-r


RUN  pip3 install --upgrade pip
RUN  pip3 install -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.upload_files" ]
