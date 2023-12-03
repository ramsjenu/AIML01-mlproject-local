pipeline {
    environment {
    registry = "ramsjenu/student-performance"
    registryCredential = 'dockerhub_id'
    dockerImage = ''
}

agent any

stages {
    
    stage('Building our image') {
        ageny any
        steps{
            script {
                dockerImage = docker.build registry + ":$BUILD_NUMBER"
            }
        }
    }
    
    stage('Deploy our image') {
        agent any
        steps{
            script {
                docker.withRegistry( '', registryCredential ) {
                dockerImage.push()
                }
            }
        }
    } 
}
}
