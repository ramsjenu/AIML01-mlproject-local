pipeline {
    agent any
    environment {
        DOCKER_HUB_ID ="ramsjenu"
        IMAGE_REPO_NAME="student-performance"
        IMAGE_TAG="latest"
        REPOSITORY_URI = "${DOCKER_HUB_ID}/${IMAGE_REPO_NAME}"
    }

    stages {
   
    // Building Docker images
      stage('Building image') {
      steps{
        script {
          dockerImage = docker.build "${IMAGE_REPO_NAME}:${IMAGE_TAG}"
        }
      }
    }
   
    // Uploading Docker images into AWS ECR
    stage('Pushing to Docker-Hub') {
      steps{  
         script {
                sh "docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:$IMAGE_TAG"
                sh "docker push ${REPOSITORY_URI}:$IMAGE_TAG""
         }
      }
    }
    stage('Creating Container') {
      steps{  
         script {
                 sh "docker run --name=studperfml -d -p 8081:8080 --ipc='host' $REPOSITORY_URI:$IMAGE_TAG"
         }
      } 
    }        
  }
}
