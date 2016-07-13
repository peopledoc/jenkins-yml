#!/bin/bash

set -eux

cd sandbox/

teardown() {
    rm -vf _job

    [ $1 -eq 0 ] && : OK || : FAIL

    return $1
}

trap 'teardown $?' DEBUG

! jenkins-yml-runner
JOB_NAME=undefined jenkins-yml-runner
JOB_NAME=simple jenkins-yml-runner |& grep -C 10 simple
! JOB_NAME=missing-script jenkins-yml-runner
JOB_NAME=script jenkins-yml-runner
JOB_NAME=overwrite-runner jenkins-yml-runner
! JOB_NAME=overwrite-runner-inexistant jenkins-yml-runner
AXE1=a JOB_NAME=matrix jenkins-yml-runner
AXE1=b JOB_NAME=matrix jenkins-yml-runner
AXE1=inexistant JOB_NAME=matrix jenkins-yml-runner
! MISSING_AXE1= JOB_NAME=matrix jenkins-yml-runner

: SUCCESS