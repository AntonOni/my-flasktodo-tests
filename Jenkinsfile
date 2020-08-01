pipeline {
    agent { label 'master' }
    stages {
        stage ('test') {
            steps {
//                 dir ('/home/jenkins/my-flasktodo-tests'){
//                     sh 'cd /var/lib/jenkins/workspace/automation_to_do'
//                     sh 'pip3 install -r requirements.txt'
// каждый новый sh с командой открывает новое окно в консоли для выполнения действия
//                     sh 'cd /var/lib/jenkins/workspace/automation_to_do/test_ui/test_main/'
//                     sh 'python3 -m pytest /var/lib/jenkins/workspace/automation_to_do/test_ui/test_main/test_runner.py'

// если sh один с несколькими командами то все действия выполняются в одной консоли
                    sh """
                    cd /var/lib/jenkins/workspace/automation_to_do
                    source ./venv/bin/activate
                    pip3 install -r requirements.txt
                    cd /var/lib/jenkins/workspace/automation_to_do/test_ui/test_main/
                    python3 -m pytest test_runner.py
                    """
            }
        }
    }
}


