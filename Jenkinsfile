pipeline {
    environment {
    registry = "ramsjenu/student-performance"
    dockerCredentialsId = 'dockerhub-credentials-id'
    dockerImage = ''
}

agent any

stages {
    
    stage('Building our image') {
        steps{
            script {
                dockerImage = docker.build registry + ":$BUILD_NUMBER"
            }
        }
    }
    
    // Uploading Docker images into AWS ECR
    stage('Pushing to Docker-Hub') {
        steps{  
            script { 
                sh "docker push $registry:$BUILD_NUMBER"
            }
        }
    }
    
    stage('Pulling the latest image') {
        steps{  
            script { 
                sh "docker pull $registry:$BUILD_NUMBER"
            }
        }
    }
    stage('Creating Container') {
      steps{  
         script { 
                 sh "docker run --name=spml -d -p 8085:8080 --ipc='host' $registry:$BUILD_NUMBER"
         }
      } 
    }        
}
}
