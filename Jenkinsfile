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
          sh 'sudo pip install -r /var/lib/jenkins/workspace/student-performance/requirements.txt'
          sh 'python /var/lib/jenkins/workspace/student-performance/app.py'
      }
     }
   }
 }
}  
