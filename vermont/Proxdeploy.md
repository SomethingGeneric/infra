# Promox New VM Deploy
1. Copy template VM
2. Get avail IP address from spreadsheet
3. Reserve a (temp) IP address in pihole by MAC addr
3. SSH to machine (on temp addr), change hostname, set permanent IP address, and passwordless sudo
4. Remove temp ip in pihole
4. SSH key add
5. Update `hosts.ini`
6. Run qemu agent deploy, wazuh agent deploy, snmp deploy
7. Done?