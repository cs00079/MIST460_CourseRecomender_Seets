#!/bin/bash
cd /home/site/wwwroot/API
exec uvicorn course_recommender_api:app --host 0.0.0.0 --port 8000