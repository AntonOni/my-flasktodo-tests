pipeline {
    agent none

    stages {

        stage ('Hello') {
            agent any

            steps {
                sh 'cd /home/ec2-user/my-flasktodo-tests'
                sh 'git checkout master'
                sh 'git pull'
                sh 'python3 -m pip install --user -r requirements.txt'
                sh 'cd /home/ec2-user/my-flasktodo-tests/test_ui/test_main'
                sh 'pytest test_runner.py'
            }
        }
    }
}