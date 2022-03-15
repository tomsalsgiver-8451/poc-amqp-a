# AMQP 1.0 PoC Service A
A test service for interacting with an AMQP 1.0 compliant broker.
Sends messages on the queue **poc-b** and waits to receive back a modified version on the **poc-a** queue.

## Docker Setup
#### Install Docker
`brew install --cask docker`

#### Create RabbitMQ Container
`docker-compose up -d`

If you run into the error: **filesystem layer verification failed for digest sha256**
then disable the VPN and execute the command.

## Install Required Services
#### Create a virtual environment
`python3 -m venv env`

#### Activate it
`source env/bin/activate`

#### Install qpid-proton
`pip3 install python-qpid-proton`


## Running the service
`./run_app.sh`

This will start up FastAPI on localhost:80 with qpid proton integrated.
Send a POST on the /send endpoint using the input_model contract and receive back a modified object.

## Viewing the Broker
Once the docker container is spun up, the broker will be running a management portal on localhost:15672.
The default user and password is guest/guest.

