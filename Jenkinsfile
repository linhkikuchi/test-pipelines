pipeline {
    agent {
        label "master"
    }
    options {
        ansiColor("xterm")
        timeout(time: 5, unit: "MINUTES")
        timestamps()
    }
    parameters {
        string(name: "BRANCH")
    }
    stages {
        stage("stage1") {
            steps {
                script {
                    loadScripts()
                    common.mycommoncode()
                }
            }
        }
        stage("stage2") {
            steps {
                script {
                    common.mycommoncode2()
                }
            }
        }
        stage("stage3") {
            steps {
                echo "${BRANCH}"
            }
        }
    }
}

def loadScripts() {
    common = load "common.groovy"
}
