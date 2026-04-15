#!/bin/bash
cd /tmp/8de9b3f64630d24
exec uvicorn course_recommender_api:app --host 0.0.0.0 --port 8000