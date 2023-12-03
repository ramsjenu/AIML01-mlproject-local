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
    
    stage('Deploy our image') {
        steps{
            script {
                docker.withRegistry( '', registryCredential ) {
                dockerImage.push()
                }
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
