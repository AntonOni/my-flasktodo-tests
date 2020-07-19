pipeline {
    agent { label 'master' }
    stages {
        stage ('build') {
            steps {
                dir ('/home/ec2-user/my-flasktodo-tests'){
                    sh 'sudo pwd'
                    sh 'sudo python3 -m pip install --user -r requirements.txt'
                    sh 'sudo cd /test_ui/test_main'
                    sh 'sudo pytest test_runner.py'
                }
            }
        }
    }
}

