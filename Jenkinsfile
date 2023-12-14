pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & SonarQube Analysis') {
            steps {
                withMaven(maven: 'Maven') {
                    sh 'mvn clean package sonar:sonar'
                }
            }
        }

        // Другие этапы, такие как тестирование, деплой и т.д.
    }

    post {
        always {
            echo 'Pipeline execution complete!'
        }
    }
}
