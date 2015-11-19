import os
import re
import time
import errno
import argparse
import requests


def check_name(name):
    if not re.match(r"^\w[-\.\w]*$", name):
        raise RuntimeError("invalid name '{0}'".format(name))
    return name


def make_tag():
    return time.strftime("%Y%m%d-%H%M%S")


def main():
    parser = argparse.ArgumentParser(description="Backup GitHub repositories")
    parser.add_argument("token", metavar="TOKEN", help="GitHub API token")
    parser.add_argument("username", metavar="USERNAME", help="project username")
    parser.add_argument("reponame", metavar="REPONAME", help="project reponame")
    parser.add_argument("artifacts", metavar="ARTIFACT", help="the artifact directory", nargs="+")
    args = parser.parse_args()

    username = check_name(args.username)
    reponame = check_name(args.reponame)
    tag = make_tag()

    response = requests.post(
        "https://api.github.com/repos/{0}/{1}/releases".format(username, reponame),
        json={
            "tag_name": tag,
            "body": "Generated release {0}.".format(tag),
            "name": tag
        },
        headers={
            "Authorization": "token {0}".format(args.token)
        }
    )
    response.raise_for_status()
    release = response.json()
    print "Generated release {0}".format(release["name"])

    # upload_url is given in uri-template form. We could
    # use a package for this...
    upload_url, _, _ = release["upload_url"].partition("{")

    for artifact in args.artifacts:
        with open(artifact, "rb") as artifact_file:
            response = requests.post(
                upload_url,
                data=artifact_file,
                params={
                    "name": os.path.basename(artifact)
                },
                headers={
                    "Authorization": "token {0}".format(args.token),
                    "Content-Type": "application/octet-stream"
                }
            )
            response.raise_for_status()
        print "Uploaded", artifact

if __name__ == "__main__":
    main()