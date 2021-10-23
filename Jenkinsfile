pipeline {
    agent { dockerfile true }
    stages {
          stage ("Test"){
            steps{
                echo "verify"
                //sh 'ifconfig'
                sh 'python manage.py runserver &'
                sh "curl http://172.17.0.2:8000" 
            }
        }
    }
}

