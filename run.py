#!/usr/bin/python

from app import views
from app.views import app

if __name__ == "__main__":
    app.run(host="10.0.60.106",port=5000) 
