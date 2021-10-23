pipeline {
    agent {
        docker {
            label 'service'
            alwaysPull false
            registryUrl "https://hub.docker.com/repository/docker"
            registryCredentialsId "tayssirboubaker"
            image 'tayssirboubaker/docker-django-v0.0:latest'
            args '-v /var/run/docker.sock:/var/run/docker.sock --network host'
        }    
    stages{
        stage ("cloning") {
            steps{
                echo "cloning"
               sh "git clone https://github.com/Taysssir/GoMyCodeLabProject.git"
            }
        }
        stage ("Install dependenciess"){
            steps{
                echo "installing dependencies"
                sh "cd GoMyCodeLabProject && pip3 install -r requirments.txt"
            }
        }
        stage ("System check"){
            steps{
                echo "Test project"
                sh " cd GoMyCodeLabProject && python3 manage.py test"
            }
        }
            stage ("Deploy"){
            steps{
                echo "start project"
                sh " cd GoMyCodeLabProject && python3 manage.py runserver "
                //sh " cd GoMyCodeLabProject && python3 manage.py runserver --"
            }
        }
        stage ("Test"){
            steps{
                echo "verify"
                sh "curl http://127.0.0.1:8000" 
            }
        }

    }
    
}
