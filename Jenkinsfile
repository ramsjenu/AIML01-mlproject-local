pipeline {
    environment {
    registry = "ramsjenu/student-performance"
    registryCredential = 'dockerhub_id'
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
                // sh "docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:$IMAGE_TAG"
                sh "docker login registryCredential"
                sh "docker push ${registry + ':$BUILD_NUMBER'"
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
