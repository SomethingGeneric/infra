#!/usr/bin/env bash

cd /home/matt/infra/vermont/renovate

[[ ! -d venv ]] && python3 -m venv venv && venv/bin/pip install requests
venv/bin/python3 get_repos.py

echo "Updated list of repos"

export PATH="/usr/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH"
export RENOVATE_CONFIG_FILE="/home/matt/renovate/config.js"

export LOG_LEVEL="debug"

# hidden secret things (github token and forgejo token)
[[ -f .variables.sh ]] && source .variables.sh

echo "Spawning renovate"

renovate
