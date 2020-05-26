#!/bin/bash
if [ ! -d '.env' ]
then
    echo "No environment file detected, creating virtual environment..."

    if ! command -v virtualenv
    then
        echo "virtualenv is not installed. Please install by typing 'pip3 install virtualenv' and try again"
        exit 1
    fi

    virtualenv ./.env
    source ./.env/bin/activate

    sleep 1s
    echo "Installing requirements"
    pip install -r requirements.txt
    
    echo "\nVirtual environment is created and established"
    
else
    echo "Virtual environment found."
    . ./.env/bin/activate
    echo "Switching"

fi

driver() {
    python -i driver.py
}

run() {
    python fish_tank.py
}

stop() {
    unset -f stop run driver
    deactivate
}
