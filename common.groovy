#!/usr/bin/env groovy

def mycommoncode(){
    catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
        sh "echo Test1"
    }
}


def mycommoncode2() {
    catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
        sh """
            echo Test2
        """
    }
}

return this
