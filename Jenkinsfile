pipeline {
    environment {
    registry = "ramsjenu/student-performance"
    dockerImage = ''
}

agent any

stages {
    
    stage('Building our image') {
        steps{
            script {
                dockerImage = docker.build registry + ":latest"
            }
        }
    }
    
    // Uploading Docker images into AWS ECR
    stage('Pushing to Docker-Hub') {
        steps{  
            script { 
                sh "docker push $registry:latest"
            }
        }
    }
    
    stage('Pulling the latest image') {
        steps{  
            script { 
                sh "docker pull $registry:latest"
            }
        }
    }
    stage('Creating Container') {
      steps{  
         script { 
                 sh "docker run --name=spml -d -p 8083:8080 --ipc='host' $registry:latest"
         }
      } 
    }        
}
}
