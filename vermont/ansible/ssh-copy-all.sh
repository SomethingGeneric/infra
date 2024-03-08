#!/usr/bin/env bash
for h in $(cat hosts.ini | egrep -o "10.0.1.[0-9]+"); do ping -c 1 $h && ssh-copy-id $h; done
