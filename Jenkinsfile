pipeline {
    agent { label 'master' }
    stages {
        stage ('build') {
            steps {
                dir ('/home/jenkins/my-flasktodo-tests'){
//                     sh 'sudo yum install python36-pip'
//                     sh 'pip install -r requirements.txt'
                    sh 'cd ./test_ui/test_main'
                    sh 'python -m pytest /home/jenkins/my-flasktodo-tests/test_ui/test_main/test_runner.py'
                }
            }
        }
    }
}

"""
Нужно установать пип3 под юзером дженкинс
"""