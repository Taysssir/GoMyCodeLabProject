pipeline {
    agent { dockerfile true }
    stages {
        stage('Build Image ') {
            steps {
                sh 'docker build -t docker-django-v0.0 .'
            }
         }
        stage('Run Image ') {
            steps {
                sh 'docker run docker-django-v0.0'
            }
        }
       stage('Show Containers ') {
            steps {
                sh 'docker ps'
            }
        }
    }
}
