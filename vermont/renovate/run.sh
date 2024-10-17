#!/usr/bin/env bash

cd /home/matt/infra/vermont/renovate

# hidden secret things (github token and forgejo token)
[[ -f .variables.sh ]] && source .variables.sh

[[ ! -d venv ]] && python3 -m venv venv && venv/bin/pip install requests
venv/bin/python3 get_repos.py

echo "Updated list of repos"

export LOG_LEVEL="debug"

echo "Spawning renovate"

docker run --rm -e GITHUB_COM_TOKEN -e RENOVATE_TOKEN -e LOG_LEVEL -v "./config.js:/usr/src/app/config.js" renovate/renovate
