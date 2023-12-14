pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Клонирование кода из GitHub репозитория
                git 'https://github.com/Strevochka/pet-project.git'
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image('myapp-test-image').inside {
                        // Запуск pylint
                        sh 'pylint version'
                        // Другие команды тестирования
                    }
                }
            }
        }
    }
}
