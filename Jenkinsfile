pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Building Environment...'
                sh 'python3 --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Running Unit Tests...'
                sh 'python3 test_app.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to Production...'
                sh 'python3 app.py'
            }
        }
    }
}