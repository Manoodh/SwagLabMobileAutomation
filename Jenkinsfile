pipeline {
    agent any

    stages {
        stage('🚀 Fetch Repository Workspace') {
            steps {
                echo 'Checking out the latest automation codebase from GitHub source control...'
                checkout scm
            }
        }

        stage('📦 Install Framework Dependencies') {
            steps {
                echo 'Verifying environment requirements and pulling Python testing libraries...'
                bat 'pip install --user pytest Appium-Python-Client selenium'
            }
        }

        stage('🧪 Execute Appium Mobile Regression') {
            steps {
                echo 'Routing automated script requests to local Appium infrastructure listener...'
                // -v: Verbose output tracking steps
                // -s: Capture and display custom stdout console prints in Jenkins log
                bat 'python -m pytest -v -s tests/testsauceapp.py'
            }
        }
    }

    post {
        always {
            echo 'Test cycle execution finished. Cleaning up workspace context elements...'
        }
        success {
            echo '🎉 All automated mobile validation checkpoints passed cleanly!'
        }
        failure {
            echo '❌ Pipeline execution checkpoint failed! Review the console logs above to diagnose element timeouts or driver errors.'
        }
    }
}