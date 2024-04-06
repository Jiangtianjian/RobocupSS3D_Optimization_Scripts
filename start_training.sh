#!/bin/bash
###########################################
# Starts the players for penalties.
# Example: bash start_penalty.sh localhost
###########################################
export SPARK_SERVERPORT=$[$RANDOM + 1025] #3200
export SPARK_AGENTPORT=$[$RANDOM + 1025] #3100

rcssserver3d --agent-port $SPARK_AGENTPORT --server-port $SPARK_SERVERPORT &
PID=$!
<roboviz shell> --serverPort=$SPARK_SERVERPORT &
# replace the <roboviz shell> with the Roboviz Starter if you want to check the performance of the parameters
# such as /home/apollo3d/RoboViz/bin/roboviz.sh --serverPort=$SPARK_SERVERPORT &
PID2=$!

sleep 5
DIR_SCRIPT="$( cd "$( dirname "$0" )" && pwd )" 

DIR_PARAMS="$( cd "$( dirname "$1" )" && pwd )"
DIR_OUTPUT="$( cd "$( dirname "$2" )" && pwd )"
PARAMS_FILE=$DIR_PARAMS/$(basename $1)
OUTPUT_FILE=$DIR_OUTPUT/$(basename $2)

echo "$PARAMS_FILE!"

mkdir -p log
cd $DIR_SCRIPT
today=`date +%Y-%m-%d-%H-%M-%S`

java -cp "$DIR_SCRIPT/lib/*" magma.robots.RoboCupClient --playerid=3 --factory=TrainingKick8M --port=$SPARK_AGENTPORT --monitorport=$SPARK_SERVERPORT --server=127.0.0.1 --inputFile=$PARAMS_FILE --outFile=$OUTPUT_FILE --decisionmaker=TrainKick8m 1>log/outAndError$today.log 2>&1 &

AGENTPID=$!
sleep 3

maxWaitTimeSecs=1200
total_wait_time=0

while [ ! -f $OUTPUT_FILE ] && [ $total_wait_time -lt $maxWaitTimeSecs ]
do 
  sleep 1
  total_wait_time=`expr $total_wait_time + 1`
done 

if [ ! -f $OUTPUT_FILE ]
then
  echo "Timed out while waiting for script to complete, current wait time is $total_wait_time seconds."
else
  echo "Completed with a wait time of $total_wait_time seconds."
fi

echo "Killing Simulator"
kill -s 2 $PID $PID2
echo "Killing Agent"
kill -s 2 $AGENTPID

sleep 2
echo "Finished"

