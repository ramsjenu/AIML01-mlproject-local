pipeline {
  agent {
    any
  }
  stages {  // Define the individual processes, or stages, of your CI pipeline
    stage('Checkout') { // Checkout (git clone ...) the projects repository
      steps {
        checkout scm #
      }
    }
    stage('Setup') { // Install any dependencies you need to perform testing
      steps {
        script {
          sh 'pip install -r requirements.txt'
          sh 'python app.py'
      }
     }
   }
 }
}  
