import os
import requests
import fileinput

BASE_URL = "https://git.goober.cloud/api/v1"
USERNAME = "renovate"
TOKEN = os.getenv("RENOVATE_TOKEN")


def get_user_orgs(username):
    url = f"{BASE_URL}/users/{username}/orgs"
    headers = {"Authorization": f"token {TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        orgs = response.json()
        return [org["username"] for org in orgs]
    else:
        print(f"Error fetching orgs for user {username}:", response.text)
        return []


def get_repositories_for_user(username):
    url = f"{BASE_URL}/users/{username}/repos"
    headers = {"Authorization": f"token {TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repos = response.json()
        return [f"{username}/{repo['name']}" for repo in repos if not repo["private"]]
    else:
        print(f"Error fetching repositories for {username}:", response.text)
        return []


def get_all_users():
    url = f"{BASE_URL}/admin/users"
    headers = {"Authorization": f"token {TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        users = response.json()
        return [user["username"] for user in users]
    else:
        print("Error fetching users:", response.text)
        return []


def main():

    all_repos = []
    ignore_namespaces = ["techjournals", "others", "mattc-old"]
    ignore_parts = ["pkgbuild."]

    # Get all users
    all_users = get_all_users()
    #print("All Users:")
    for user in all_users:
        #print(user)

        # Get user's own repositories
        user_repos = get_repositories_for_user(user)
        #print("User Repositories:")
        for repo in user_repos:
            #print(repo)
            all_repos.append(repo)

        # Get repositories for each organization the user is part of
        orgs = get_user_orgs(user)
        for org in orgs:
            if org in ignore_namespaces:
                continue
            org_repos = get_repositories_for_user(org)
            #print(f"\nRepositories for Organization {org}:")
            for repo in org_repos:
                #print(repo)
                if any(part in repo for part in ignore_parts):
                    continue
                all_repos.append(repo)
        #print()

    fstr = "\"repositories\": [" + ", ".join([f"\"{repo}\"" for repo in all_repos]) + "],\n"

    # Specify the path to the config.js file
    config_file = "config.js"

    # Read the contents of the file
    with fileinput.FileInput(config_file, inplace=True) as file:
        for line in file:
            if line.startswith("repositories"):
                # Replace the line with the contents of fstr
                print(fstr.strip())
            else:
                print(line, end="")
    

if __name__ == "__main__":
    main()
