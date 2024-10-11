# Serverless Application using AWS (Lambda, Docker, ECR, RDS, API Gateway)

## Project Overview

The purpose of this project is to build a serverless application using AWS, designed to be cost-effective and scalable for small applications. The core components include:

- **Amazon RDS**: A PostgreSQL database hosted on AWS RDS, handled in a separate repository. For more details on the database setup, you can access the RDS repository here:
  - **[AWS RDS Database Repository](https://github.com/Nivix047/aws-serverless-ecom-platform-db)**
- **AWS Lambda**: CRUD functions containerized using Docker and managed via AWS ECR.
- **AWS API Gateway**: Exposing the Lambda functions as API endpoints to interact with the application.

The project setup leverages modern cloud tools to create a serverless architecture, making the CRUD functions readily available as an API in a scalable structure. This approach is ideal for minimizing costs while ensuring efficient data handling.

## Project Flow

1. **GitHub Repository (Lambda Function Code)**

   - The process starts with code being committed to the GitHub repository specifically for Lambda functions.

2. **Trigger CI/CD Pipeline**

   - A CI/CD pipeline is automatically triggered upon code commit to the main branch. This pipeline uses GitHub Actions to streamline the process.

3. **Docker Image Build and Push**

   - The pipeline sets up Docker and builds the Docker image for the Lambda function.
   - The image is then tagged and pushed to Amazon Elastic Container Registry (ECR), making it accessible for deployment.

4. **AWS Lambda Function**

   - AWS Lambda pulls the Docker image from ECR to execute the code.
   - The Lambda function uses connection strings to securely connect and perform CRUD operations on the Amazon RDS database.

5. **AWS API Gateway Integration**

   - The Lambda function is integrated with AWS API Gateway to create REST API endpoints.
   - The API Gateway handles incoming HTTP requests and triggers the Lambda function to perform the required operations.

6. **User Interaction**
   - Users interact with the API Gateway, which triggers the Lambda function to execute CRUD operations on the database via the connection to Amazon RDS.

## API Call Example

Below is an example of a successful API call to the Lambda function using AWS API Gateway, demonstrating a CRUD operation.

![API Call Example](https://github.com/user-attachments/assets/bfb620d2-7249-41a7-81c8-91828b0bc5a9)

## Key Technologies Used

- **Amazon RDS**: Relational Database Service for database management.
- **AWS Lambda**: Serverless compute service to run code without managing servers.
- **Docker**: For containerizing the application.
- **Amazon ECR**: Elastic Container Registry for storing and managing Docker images.
- **AWS API Gateway**: To create, publish, maintain, monitor, and secure APIs at scale.
- **GitHub Actions**: For setting up the CI/CD pipeline.

## Purpose of the Project

The aim of this project is to create a serverless application that is:

- **Cost-effective**: Suitable for small-scale applications.
- **Scalable**: Easily extendable as demand increases.
- **Simple Architecture**: Focuses on using AWS tools efficiently to keep the architecture straightforward and easy to manage.

The project involves setting up an RDS instance and connecting it with Lambda functions via API Gateway, providing a smooth serverless experience.

## Getting Started

1. Clone the repositories for the RDS setup and Lambda functions.
2. Follow the instructions in each repository's README to deploy the components.
3. Trigger the CI/CD pipeline by committing code changes to automate the build and deployment process.

## Contributing

Feel free to submit issues or pull requests if you find bugs or have suggestions to improve the project.

## Feedback

Always open to feedback and looking forward to connecting with professionals in the tech space!
