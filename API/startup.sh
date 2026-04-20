#!/bin/sh
gunicorn -w 4 -k uvicorn.workers.UvicornWorker course_recommender_api:app