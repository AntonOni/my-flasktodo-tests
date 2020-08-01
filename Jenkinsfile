pipeline {
    agent { label 'master' }
    stages {
        stage ('test') {
            steps {
//                 dir ('/home/jenkins/my-flasktodo-tests'){
//                     sh 'sudo apt install python3-pip'
//                     sh 'cd /var/lib/jenkins/workspace/automation_to_do'
//                     sh 'pip3 install -r requirements.txt'
                    sh 'cd /var/lib/jenkins/workspace/automation_to_do/test_ui/test_main/'
                    sh 'python3 -m pytest test_runner.py'
//                        sh """
//                        cd /var/lib/jenkins/workspace/automation_to_do/test_ui/test_main/
//                        python3 -m pytest /var/lib/jenkins/workspace/automation_to_do/test_ui/test_main/test_runner.py
//                        """
            }
        }
    }
}


