pipeline {
    agent { label 'master' }
    stages {
        stage ('build') {
            steps {
                dir ('/home/jenkins/my-flasktodo-tests'){
                    sh 'pwd'
                    sh 'python3 -m pip3 install --user -r requirements.txt'
                    sh 'cd ./test_ui/test_main'
                    sh 'python3 -m pytest ./test_runner.py'
                }
            }
        }
    }
}

