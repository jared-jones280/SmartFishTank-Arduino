# Smart Fish Tank Webserver
The Web Server for the Smart Fish Tank Monitoring System

## Installing
#### Using  `env.sh` script
1. Run `$ source env.sh`
2. Type `$ stop` to deactivate environment
#### Manual
1. Install virtualenv: `$ pip install virtualenv`
2. Create virtualenv: `$ virtualenv .env`
3. Activate virtualenv: `$ source .env/bin/activate`
4. Install python required libraries with `$ pip install -r requirements.txt`
---
## Run
- With __env.sh__ running: `$ run`
- Manually with virtualenv activated: "$ python fish_tank_server.py`
