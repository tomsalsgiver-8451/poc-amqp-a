#!/bin/bash

# Start the api
uvicorn app.main:app --host 0.0.0.0 --port 80 --proxy-headers
