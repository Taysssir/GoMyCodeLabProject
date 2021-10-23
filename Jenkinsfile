pipeline {
    agent { dockerfile true }
    stages {
        stage('Build Image ') {
            steps {
                echo 'List all images' 
                //sh 'docker image ls'
                //sh 'docker build -t docker-django-v0.0 .'
                echo 'Try run image'
                //sh 'docker build -t 8a80db88f2a28d048df1b5b34d8e1dfb5fbbf20d:latest .'
            }
         }
     /*   stage('Run Image ') {
            steps {
                //sh 'docker run docker-django-v0.0'
                sh 'docker run 8a80db88f2a28d048df1b5b34d8e1dfb5fbbf20d:latest'
            }
        }
       stage('Show Containers ') {
            steps {
                sh 'docker ps'
            }
        }*/
          stage ("Test"){
            steps{
                echo "verify"
                //sh 'ifconfig'
                sh "curl http://172.17.0.2:8000" 
            }
        }
    }
}

