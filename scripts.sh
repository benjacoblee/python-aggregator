#!/bin/bash

echo "Executing script.."
source /home/benn/.virtualenvs/my_django_env/bin/activate
python3 /mnt/c/Users/User/Documents/code/projects/python-aggregator/aggregate.py
python3 /mnt/c/Users/User/Documents/code/projects/python-aggregator/send_mail.py
echo "Script completed."
rm /mnt/c/Users/User/Documents/code/projects/python-aggregator/feed.html
echo "Cleanup complete!"