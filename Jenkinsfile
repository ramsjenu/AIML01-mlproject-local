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
          sh 'source /usr/lib/python3.10/venv/.venv/bin/activate'
          sh 'pip install -r requirements.txt'
          sh 'python app.py'
      }
     }
   }
 }
}  
