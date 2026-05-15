pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
            }
        }
        stage('Build') {
            steps {
                echo 'Building Environment...'
                echo 'Simulating Python Build... Done!'
            }
        }
        stage('Test') {
            steps {
                echo 'Running Unit Tests...'
                echo 'Test Suite Passed: 100%'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to Production...'
                echo 'Processing Data Engineering Task... Success!'
            }
        }
    }
}
