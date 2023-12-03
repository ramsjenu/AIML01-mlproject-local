pipeline {
    environment {
    registry = "ramsjenu/student-performance"
    registryCredential = 'dockerhub_id'
    doc_user = 'DOCKER_USER'
    doc_pwd = 'DOCKER_PWD'
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
                sh "docker context use desktop-linux"
                docker.withRegistry( '', registryCredential ) 
                { dockerImage.push() }
            }
        }
    }

    stage('Creating Container') {
      steps{  
         script {
                 sh "docker run --name=spml -d -p 8084:8080 --ipc='host' $registry + ':$BUILD_NUMBER'"
         }
      } 
    }        
}
}
