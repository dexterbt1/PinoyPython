#!/bin/bash
set -e
virtualenv --no-site-packages --distribute ppugweb
pip install -E ppugweb -r pip-requirements.txt
