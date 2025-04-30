print ("Wassup Buddy!! v7711-baba")

pipeline {
    agent any

    environment {
        MAVEN_VERSION = '3.9.6'
    }

        stage('Install Maven') {
            steps {
                sh '''
                if ! [ -x "$(command -v mvn)" ]; then
                    echo "Installing Maven..."
                    wget https://downloads.apache.org/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz
                    tar xzf apache-maven-${MAVEN_VERSION}-bin.tar.gz
                    sudo mv apache-maven-${MAVEN_VERSION} /opt/maven
                    export PATH=/opt/maven/bin:$PATH
                    echo "export PATH=/opt/maven/bin:$PATH" >> ~/.bashrc
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


