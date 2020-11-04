#!/bin/bash

echo "Beginning execution"
source /home/benn/.virtualenvs/my_django_env/bin/activate
python3 /mnt/c/Users/User/Documents/code/projects/python-aggregator/aggregate.py
python3 /mnt/c/Users/User/Documents/code/projects/python-aggregator/send_mail.py
echo "Script completed"