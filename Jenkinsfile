pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    bat 'docker-compose build'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    bat 'docker-compose run web python -m unittest discover'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    bat 'docker-compose up -d'
                }
            }
        }
    }
}
