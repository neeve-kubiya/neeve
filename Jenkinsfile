pipeline {
    agent {
        kubernetes {
            yaml '''
                apiVersion: v1
                kind: Pod
                spec:
                  containers:
                  - name: python
                    image: python:3.9
                    command:
                    - cat
                    tty: true
            '''
            defaultContainer 'python'
        }
    }
    environment {
        WEBHOOK_URL = "https://webhooksource-kubiya.hooks.kubiya.ai:8443/lZ1-aSoPoOzv5IlZ1hiCDoT5WqObjqs4PpnMWvEKoXnrHIAU-FZ67V_iYTEwNvdanC6mK_WfqDQOzgjoa6B32-4="
        WORKSPACE = "/home/jenkins/agent/workspace/${env.JOB_NAME}"
    }
    stages {
        stage('Check Event Type') {
            steps {
                script {
                    def webhookEvent = env.GITHUB_EVENT ?: 'unknown'
                    echo "Webhook event: ${webhookEvent}"
                    
                    if (webhookEvent != 'opened') {
                        echo "Skipping build - not a PR opened event (Event: ${webhookEvent})"
                        currentBuild.result = 'ABORTED'
                        error('Build skipped - not a PR opened event')
                    }
                }
            }
        }
        stage('Checkout') {
            steps {
                script {
                    // Handle both SCM-triggered and manual builds
                    def repoUrl = scm.userRemoteConfigs ? scm.userRemoteConfigs[0].url : params.GIT_REPO_URL
                    def branch = env.GIT_BRANCH ?: params.BRANCH_NAME ?: 'main'

                    echo "Cloning repository: ${repoUrl} on branch: ${branch}"
                    echo "Using workspace: ${WORKSPACE}"

                    // Ensure we're in the correct workspace
                    dir("${WORKSPACE}") {
                        checkout([
                            $class: 'GitSCM',
                            branches: [[name: "${branch}"]],
                            userRemoteConfigs: [[
                                url: repoUrl,
                                credentialsId: 'github-access'
                            ]]
                        ])
                    }
                }
            }
        }
        stage('Build & Test') {
            steps {
                script {
                    dir("${WORKSPACE}") {
                        if (fileExists('build.sh')) {
                            echo "Executing build.sh..."
                            sh 'chmod +x build.sh && ./build.sh'
                        } else {
                            echo "No build script found. Simulating failure."
                            sh 'exit 1'
                        }
                    }
                }
            }
        }
    }
    post {
        failure {
            script {
                def repoUrl = scm.userRemoteConfigs ? scm.userRemoteConfigs[0].url : params.GIT_REPO_URL
                def commit = env.GIT_COMMIT ?: 'unknown'
                def jobName = env.JOB_NAME
                def buildUrl = env.BUILD_URL
                def buildNumber = env.BUILD_NUMBER
                def branch = env.GIT_BRANCH ?: params.BRANCH_NAME ?: 'main'
                def failureTime = new Date().format("yyyy-MM-dd'T'HH:mm:ss'Z'", TimeZone.getTimeZone('UTC'))

                // Extract repository full name
                def repoFullName = env.REPO_FULL_NAME ?: 'unknown'

                // Extract PR number
                def prNumber = env.PR_NUMBER ?: env.CHANGE_ID ?: env.GITHUB_PR_NUMBER ?: 'unknown'

                // Extract commit SHA
                def commitSHA = env.GIT_COMMIT ?: env.COMMIT_SHA ?: 'unknown'

                // Extract webhook event type
                def webhookEvent = env.GITHUB_EVENT ?: 'unknown'

                echo "Webhook event: ${webhookEvent}"

                // Only proceed if this is a PR opened event
                if (webhookEvent == 'opened') {
                    echo "Processing webhook for PR opened event"
                    
                    // **Debug Logging**
                    echo "Debug values before webhook:"
                    echo "repoUrl: ${repoUrl}"
                    echo "repoFullName: ${repoFullName}"
                    echo "commitSHA: ${commitSHA}"
                    echo "branch: ${branch}"
                    echo "prNumber: ${prNumber}"
                    echo "webhookEvent: ${webhookEvent}"

                    // **Create JSON payload for Kubiya webhook**
                    def payload = groovy.json.JsonOutput.toJson([
                        build_number: buildNumber,
                        status: "FAILURE",
                        repository: repoFullName,
                        branch: branch,
                        commit_sha: commitSHA,
                        job_name: jobName,
                        build_url: buildUrl,
                        timestamp: failureTime,
                        pull_request_number: prNumber
                    ])

                    echo "Final Payload: ${payload}"

                    // Send to Kubiya webhook
                    sh """
                        curl -X POST \
                            -H 'Content-Type: application/json' \
                            -d '${payload}' \
                            '${WEBHOOK_URL}'
                    """
                } else {
                    echo "Skipping webhook - not a PR opened event (Event: ${webhookEvent})"
                }
            }
        }
    }
}
