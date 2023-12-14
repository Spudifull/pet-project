pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Извлекаем код из Git
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Добавьте команды для сборки проекта
                sh 'echo Building...'
                // Например: sh 'mvn clean package'
            }
        }

        stage('Test') {
            steps {
                // Запускаем тесты
                sh 'echo Running tests...'
                // Например: sh 'mvn test'
            }
        }

        stage('Check SonarQube Scanner') {
            steps {
                sh 'which sonar-scanner'
            }
        }

        stage('Deploy') {
            steps {
                // Деплой на тестовый сервер
                sh 'echo Deploying to test server...'
                // Добавьте команды или скрипты для деплоя
            }
        }
    }

    post {
        always {
            // Действия после завершения пайплайна, например, отправка уведомлений
            echo 'Pipeline execution complete!'
        }
    }
}
