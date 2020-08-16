pipeline {
    agent { label 'master' }
    stages {
        stage ('test') {
            steps {
// каждый новый sh с командой открывает новое окно в консоли для выполнения действия
//                     sh 'cd /var/lib/jenkins/workspace/automation_to_do/test_ui/test_main/'
//                     sh 'python3 -m pytest /var/lib/jenkins/workspace/automation_to_do/test_ui/test_main/test_runner.py'
// если sh один с несколькими командами то все действия выполняются в одной консоли
                    sh """
                    cd /var/lib/jenkins/workspace/automation_to_do
                    pip install -r requirements.txt
                    cd /var/lib/jenkins/workspace/automation_to_do/test_ui/test_main/
                    python3.7 -m pytest --alluredir="/var/lib/jenkins/workspace/automation_to_do/reports" test_runner.py
                    """
                    script {
                            allure([
                                    includeProperties: false,
                                    jdk: '',
                                    properties: [],
                                    reportBuildPolicy: 'ALWAYS',
                                    results: [[path: '/var/lib/jenkins/workspace/automation_to_do/reports']]
                                    ])
                            }
                   sh """
                   python3.7 -m allure serve /var/lib/jenkins/workspace/automation_to_do/reports
                   """
                   }
        }
    }
}


