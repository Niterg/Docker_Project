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
                    // Run tests (e.g., unit tests inside container)
                    sh 'docker-compose run web python -m unittest discover'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Run containers in detached mode
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}
