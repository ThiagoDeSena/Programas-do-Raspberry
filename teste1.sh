#!/bin/bash

AMBIENTE_VIRTUAL="/home/pi/ProgramasTestes/MariaDBeMQTT/projeto"
SCRIPT_PYTHON="/home/pi/ProgramasTestes/MariaDBeMQTT/mariaDB_and_mqtt.py"

source $AMBIENTE_VIRTUAL/bin/activate
python $SCRIPT_PYTHON
