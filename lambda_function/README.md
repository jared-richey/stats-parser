# AWS Lambda Function   

## This is an example lambda function that uses a Python runtime    

**IMPORTANT**  
* Build the layer package (pip packages used as dependencies) by running the following command:  
```docker run -v "$PWD":/var/task "public.ecr.aws/sam/build-python3.9" /bin/sh -c "pip install -r requirements.txt -t python/lib/python3.9/site-packages/; exit"```  
_Note:_ Runs the docker image used by Amazon for a specific serverless runtime and collects packages for that environment based on the requirements<span>.</span>txt file on your machine. Saves the results in a python folder which needs to be zipped with this command:  
`zip -r layer_output.zip python/`  
* Also, writes/reads from S3 using the [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html) library and serves up the file as a static website [S3 tutorial](https://docs.aws.amazon.com/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html).  
