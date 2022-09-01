# PyOrchestrator

A simple python script to run different commands on multiple servers in parallel.


## Testing in Local

To test in local we will run two docker containers on which we will be running the commands we defined in [commands.ini](./commands.ini) file.


### Requirements
* python3
* pipenv

### SetUp

Run below docker-compose to run container of openssh-server with ssh enabled.

```
docker-compose up -d --build --remove-orphans
```

Install Dependencies using pipenv

```
pipenv install
```

Running python script to connect to remote servers in [inventory.ini](./inventory.ini) and execute commands listed in commands.ini

```
pipenv run python main.py
```

### Change Commands

To change list of commands to be running on the each machine modify [commands.ini](./commands.ini)