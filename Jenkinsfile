pipeline {
    agent { label 'master' }
    stages {
        stage ('test') {
            steps {
                dir ('/home/jenkins/my-flasktodo-tests'){
                    sh 'sudo apt install python3-pip'
                    sh 'pip3 install -r requirements.txt'
                    sh 'cd ./test_ui/test_main'
                    sh 'python -m pytest /var/lib/jenkins/workspace/automation_to_do/test_ui/test_main/test_runner.py'
                }
            }
        }
    }
}

"""
Нужно установать пип3 под юзером дженкинс
"""
