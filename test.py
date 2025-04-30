pipeline {
    agent any

    environment {
        MAVEN_VERSION = '3.9.6'
    }

    stages {
        stage('Install Maven') {
            steps {
                sh '''
                echo "Wassup Buddy!! v7711-baba"
                if ! [ -x "$(command -v mvn)" ]; then
                    echo "Installing Maven..."
                    wget https://downloads.apache.org/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz
                    tar xzf apache-maven-${MAVEN_VERSION}-bin.tar.gz
                    sudo mv apache-maven-${MAVEN_VERSION} /opt/maven
                    echo "export PATH=/opt/maven/bin:$PATH" >> ~/.bashrc
                    export PATH=/opt/maven/bin:$PATH
                else
                    echo "Maven is already installed."
                fi
                mvn -version
                '''
            }
        }

        stage('Run Maven Build') {
            steps {
                sh 'mvn clean install'
            }
        }
    }

    post {
        always {
            echo 'Pipeline Finished!'
        }
    }
}
