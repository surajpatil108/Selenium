pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'ff2d33b2-10f4-47a1-b557-6531794304f5', url: 'https://github.com/surajpatil108/Selenium.git']]])
            }
        }
        
        stage('Build'){
            steps{
                git branch: 'main', credentialsId: 'ff2d33b2-10f4-47a1-b557-6531794304f5', url: 'https://github.com/surajpatil108/Selenium.git'
                sh 'python Hello.py'
            }
        }
        
        stage('Test'){
            steps{
                echo 'The job has been etsted.'
            }
        }
    }
}
