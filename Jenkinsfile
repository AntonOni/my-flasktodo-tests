pipeline {
    agent { label 'master' }
    stages {
        stage ('build') {
            steps {
                dir ('/home/jenkins/my-flasktodo-tests'){
                    sh 'sudo yum install python36-pip'
                    sh 'pip3 install -r requirements.txt'
                    sh 'cd ./test_ui/test_main'
                    sh 'python3 -m pytest ./test_runner.py'
                }
            }
        }
    }
}

