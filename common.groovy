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
