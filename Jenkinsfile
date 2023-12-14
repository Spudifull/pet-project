pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Клонирование кода из GitHub
                git 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    // Сборка Docker-образов
                    sh 'docker build -t myapp-backend -f Dockerfile.backend .'
                    sh 'docker build -t myapp-frontend -f Dockerfile.frontend .'
                }
            }
        }

        stage('Test') {
            steps {
                // Здесь добавьте команды для запуска тестов
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Запуск Docker-контейнеров
                    sh 'docker run -d -p 4000:4000 myapp-backend'
                    sh 'docker run -d -p 3000:3000 myapp-frontend'
                }
            }
        }
    }
}
