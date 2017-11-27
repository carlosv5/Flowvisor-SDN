#!/bin/bash
cd pox
xterm -e "sudo /home/ttrc/pox/pox.py openflow.of_01 --port=10001 forwarding.l2_learning  log.level --DEBUG" &
xterm -e "sudo /home/ttrc/pox/pox.py openflow.of_01 --port=10002 forwarding.l2_learning  log.level --DEBUG" &
