pipeline {
    agent any

    environment {
        // Укажите здесь переменные окружения, если они требуются
    }

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

        stage('SonarQube Analysis') {
            steps {
                // Запускаем анализ SonarQube
                withSonarQubeEnv('YourSonarQubeServerName') {
                    // Убедитесь, что sonar-scanner или maven sonar:sonar настроены правильно
                    sh 'sonar-scanner'
                }
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
