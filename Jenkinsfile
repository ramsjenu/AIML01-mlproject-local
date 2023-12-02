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
    
    stage('Cleaning up') {
        steps{
            sh "docker rmi $registry:$BUILD_NUMBER"
        }
    }
    
    stage('Creating Container') {
        steps{  
            script {
                 sh "docker run --name=studperfml -d -p 8082:8080 --ipc='192.168.0.19' $registry"
            }
        } 
    }        
}
}
