# Turteling
Creating patterns with Python turtle and ipyturtle library

# Install packages
## Create and activate virtual environment 
$ sudo apt-get install python3-venv
$ python3 -m venv venv
$ source venv/bin/activate

## Python packages
$ pip3 install -r requirements.txt
## Ubuntu needs TKinter 
$ sudo apt-get install python3-tk

# Running turtle in jupyter notebooks 
## Set extension
$ jupyter nbextension enable --py --sys-prefix ipyturtle

## Start notebook with increased data rate
$ jupyter notebook --NotebookApp.iopub_data_rate_limit=1.0e10

