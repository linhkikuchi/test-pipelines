pipeline {
    agent none
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
            	common = load "common.groovy"
                common.mycommoncode()
            }
        }
        stage("stage2") {
            steps {
            	common = load "common.groovy"
                common.mycommoncode2()
            }
        }
        stage("stage3") {
            steps {
                echo "${BRANCH}"
            }
        }
    }

}
