#!/usr/bin/env python

from withings_api.www import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)