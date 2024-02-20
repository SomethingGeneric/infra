import os
import csv
import sys

fn = "services.csv"

if len(sys.argv) > 1:
    fn = sys.argv[1]

if not os.path.exists("conf"):
    os.makedirs("conf")

base_conf = open("sample.conf").read()

ssl_domains = [
    "mattcompton.dev",
    "dizzybox.org",
    "goober.cloud",
    "champ.support"
]

with open(fn, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        domain = row[0]

        ssl_dom = None

        for dom in ssl_domains:
            if dom in domain:
                ssl_dom = dom
                break

        if ssl_dom not in ssl_domains:
            print(f"Skipping {domain}")
            print(f"SSL Domain: {ssl_dom}")
            print("No cert found.")
            exit(1)

        route = row[1]

        sn = domain

        if len(row) > 2:
            sn += " " + row[2]
        
        new = base_conf.replace("DOMAIN", sn).replace("ROUTE", route).replace("SSLNAME", ssl_dom)

        fn = domain.replace(".", "_")

        with open(f"conf/{fn}.conf", "w") as f:
            f.write(new)