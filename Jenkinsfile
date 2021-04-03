pipeline {
  agent any
  parameters {
  }
  stages {
    stage('checkout') {
           steps {  
                git branch: 'master', url: 'https://github.com/durgalakshmih/new-application.git'
          }
        }
    stage('UnitTest') {
      steps {
        sh 'unit_test.py'
      }   
    }
    stage('Build app and deploy') {
      steps {
        sh "ansible-playbook -v -C -i hosts playbooks/myapp.yaml"
      }
    }
  }
        
}
