pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker-compose build'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests (if applicable)
                    sh 'docker-compose run web python -m unittest discover'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy the application
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}