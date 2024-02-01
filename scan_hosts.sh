#!/usr/bin/env bash

printf "Net ID: "
read NETID

printf "First host (end bits): "
read FIRST

printf "Last host (end bits): "
read LAST

nmap -p 22 $NETID.$FIRST-$LAST --open | grep -oP '\d+\.\d+\.\d+\.\d+' > ssh_servers.txt