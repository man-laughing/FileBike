#!/usr/bin/python

from app import views
from app.views import app

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000) 
