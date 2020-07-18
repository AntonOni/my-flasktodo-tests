pipeline {
    agent { label 'master' }
    stages {
        stage ('build') {
            steps {
                dir ('/home/ec2-user/my-flasktodo-tests'){
                    echo "Hello World!"
                    sh 'git checkout master'
                    sh 'git pull'
                    sh 'python3 -m pip install --user -r requirements.txt'
                    sh 'cd /test_ui/test_main'
                    sh 'pytest test_runner.py'

                }
            }
        }
    }
}
