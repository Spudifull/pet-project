pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Клонирование кода из GitHub репозитория
                git 'https://github.com/Strevochka/pet-project.git'
            }
        }

        stage('Build') {
            steps {
                // Сборка Docker образа
                sh 'docker build -t myapp-backend .'
            }
        }

        stage('Deploy') {
            steps {
                // Запуск Docker контейнера
                sh 'docker run -d -p 4000:4000 myapp-backend'
            }
        }
    }
}
