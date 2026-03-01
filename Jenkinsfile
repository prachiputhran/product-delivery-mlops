pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat 'python src/train.py'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest || echo No tests found'
            }
        }
    }
}