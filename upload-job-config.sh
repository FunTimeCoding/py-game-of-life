#!/bin/sh -e

~/src/jenkins-tools/bin/delete-job.sh py-game-of-life || true
~/src/jenkins-tools/bin/put-job.sh py-game-of-life job.xml
