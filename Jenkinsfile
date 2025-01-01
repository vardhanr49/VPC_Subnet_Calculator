pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/your-username/vpc-subnet-calculator.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('vpc-subnet-calculator:latest')
                }
            }
        }
        stage('Push to ECR') {
            steps {
                script {
                    sh '''
                    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.us-east-1.amazonaws.com
                    docker tag vpc-subnet-calculator:latest <your-account-id>.dkr.ecr.us-east-1.amazonaws.com/vpc-subnet-calculator:latest
                    docker push <your-account-id>.dkr.ecr.us-east-1.amazonaws.com/vpc-subnet-calculator:latest
                    '''
                }
            }
        }
        stage('Deploy to ECS') {
            steps {
                script {
                    sh '''
                    aws ecs update-service --cluster <your-cluster-name> --service <your-service-name> --force-new-deployment
                    '''
                }
            }
        }
    }
}
