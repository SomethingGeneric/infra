import os

content = []
istr = "- import_playbook: "

ignore = [
    "kubernetes.yml",
    "maybe.yml",
    "update.yml",
    "main.yml",
]

for file in os.listdir("."):
    if file.endswith(".yml") and file not in ignore:
        content.append(istr + file)

with open("main.yml", "w") as f:
    f.write("---\n")
    f.write("\n".join(content))