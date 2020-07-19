pipeline {
    agent { label 'master' }
    stages {
        stage ('build') {
            steps {
                dir ('/home/jenkins'){
                    sh 'pwd'
                    sh 'python3 -m pip install --user -r requirements.txt'
                    sh 'cd /test_ui/test_main'
                    sh 'pytest test_runner.py'
                }
            }
        }
    }
}

