import os
import csv

if not os.path.exists("conf"):
    os.makedirs("conf")

base_conf = open("sample.conf").read()

ssl_domains = [
    "mattcompton.dev",
    "dizzybox.org",
    "goober.cloud",
    "champ.support"
]

with open('services.csv', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        domain = row[0]

        for dom in ssl_domains:
            if dom in domain:
                ssl_dom = dom
                break

        if ssl_dom not in ssl_domains:
            print(f"Skipping {domain}")
            print(f"SSL Domain: {ssl_dom}")
            print("No cert found.")

        route = row[1]
        
        new = base_conf.replace("DOMAIN", domain).replace("ROUTE", route).replace("SSLNAME", ssl_dom)

        fn = domain.replace(".", "_")

        with open(f"conf/{fn}.conf", "w") as f:
            f.write(new)