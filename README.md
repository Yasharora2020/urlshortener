# URL Shortener

This is a URL shortener created using the Serverless Framework. The application uses AWS services, including DynamoDB, Lambda, API Gateway, and S3. The Lambda function is written in Python.

## Technologies Used

- Serverless Framework
- AWS DynamoDB
- AWS Lambda
- AWS API Gateway
- AWS S3
- Python

## Prerequisites

To deploy and use this application, you will need the following:

- AWS credentials with permissions for the above services
- Node.js and npm installed on your machine
- The Serverless Framework installed on your machine

## Installation

1. Clone the repository to your local machine:
    
        git clone   https://github.com/Yasharora2020/urlshortener.git

2. Install the dependencies:
        
        cd urlshortener
        npm install


3. Deploy the application to your AWS account:

        serverless deploy
 
4. Update the API Gateway URL in `index.html` with the URL returned by the Serverless Framework.

5. Upload the `index.html` and  'error.html' file to your S3 bucket created using the Serverless Framework:

        aws s3 cp index.html s3://<your-bucket-name>/index.html
        aws s3 cp error.html s3://<your-bucket-name>/error.html

6. Visit the URL of your S3 bucket to use the application.

## Still working on

- [ ] Improve UI
- [ ] Improve Project Structure
- [ ] Add Tests
- [ ] Add CI/CD
- [ ] Add more features
- [ ] Add more documentation
- [ ] Add Cloudfront distribution for https








