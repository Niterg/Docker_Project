pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-app"
        IMAGE_TAG = "version_1"
        CONTAINER_NAME = "flask-app"
        APP_PORT = "5000"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'mero_branch', url: 'https://github.com/Niterg/Docker_Project.git'
                // Replace with your actual repo and credentials if needed
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    bat "docker run -d -p ${APP_PORT}:${APP_PORT} --name ${CONTAINER_NAME} ${IMAGE_NAME}:${IMAGE_TAG}"
                    bat "timeout /t 5 >nul" // sleep 5s on Windows
                }
            }
        }

        stage('Test Flask Application') {
            steps {
                script {
                    bat "curl -f http://localhost:${APP_PORT} || exit /b 1"
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    bat "docker stop ${CONTAINER_NAME} || exit 0"
                    bat "docker rm ${CONTAINER_NAME} || exit 0"
                }
            }
        }
    }
}
