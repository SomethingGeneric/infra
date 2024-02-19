# Nginx reverse proxy files

## How to add a service
1. Edit `services.csv`
2. Add domain to `generate_configs.py` if it's new
    * And generate a wildcard cert from cloudflare
3. Run `generate_configs.py`
4. `sudo cp conf/* /etc/nginx/sites-enabled/.`
5. `sudo chown -R root:root /etc/nginx/sites-enabled`

## Domains to move
* `graphana.vt.mattcompton.dev` -> `graphana.mattcompton.dev`
* `pve1.vt.mattcomptin.dev` -> `pve.mattcompton.dev` or `pve.goober.cloud` ?

## All Domains
* `champ.support`
* `goober.cloud`
* `dizzybox.org`
* `mattcompton.dev`