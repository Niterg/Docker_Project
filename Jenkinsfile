pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    docker-compose build
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests (if applicable)
                    docker-compose run web python -m unittest discover
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy the application
                    docker-compose up -d
                }
            }
        }
    }
}
