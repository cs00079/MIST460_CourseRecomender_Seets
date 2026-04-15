#!/bin/bash

gunicorn -w 4 -k uvicorn.workers.UvicornWorker API.course_recommender_api:app