pipeline {
    agent any

    environment {
        IMAGE_NAME = "jenkins-custom:latest"
    }

    stages {
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Run Training') {
            steps {
                sh "docker run ${IMAGE_NAME}"
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub-creds') {
                        docker.image("${IMAGE_NAME}").push("latest")
                    }
                }
            }
        }
    }
}
