#!/bin/bash

project_dir=$(dirname "$(realpath $0)")
cd $project_dir
source .venv/bin/activate
cd app
python3 app.py --config="$project_dir/config.json"
