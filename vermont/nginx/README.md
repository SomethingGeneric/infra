# Nginx reverse proxy files

## How to add a service
1. Edit `services.csv`
2. Add domain to `generate_configs.py` if it's new
    * And generate a wildcard cert from cloudflare
3. Run `generate_configs.py`
4. `sudo cp conf/* /etc/nginx/sites-enabled/.`
5. `sudo chown -R root:root /etc/nginx/sites-enabled`

## Services.csv Syntax
`domain forwarded_url alias_domain`
Example: `mattcompton.dev https://your.mom:69 www.mattcompton.dev`

## Have SSL certs for
* `champ.support`
* `goober.cloud`
* `dizzybox.org`
* `mattcompton.dev`