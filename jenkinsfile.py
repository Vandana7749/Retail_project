pipeline {
    agent any
    
        environment{
            LABS = credentials('labcreds')
        }
        
        stage('Build') {
            steps {
                // Build your project (replace 'your-build-command' with the actual build command)
                echo 'build-command'
            }
        }
        
        stage('Test') {
            steps {
                // Run tests (replace 'your-test-command' with the actual test command)
                echo 'test-command'
            }
        }

        stage('UAT') {
            steps {
                // Run tests (replace 'your-test-command' with the actual test command)
                echo 'UAT-command'
            }
        }
        
        stage('Deploy') {
            steps {
                // Deploy your application (replace 'your-deploy-command' with the actual deploy command)
                echo 'deploy-command'
            }
        }
    }
    
