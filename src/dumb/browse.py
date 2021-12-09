import requests
from flask import Blueprint, render_template
from requests.exceptions import ConnectionError

from dumb.config import get_config


browse = Blueprint("browse", "browse")


@browse.route("/")
def get_catalog():
    config = get_config()
    registry = config.registry
    try:
        response = requests.get(f"{registry.url}/{registry.version}/_catalog")
    except ConnectionError:
        return f"Cannot reach {registry.url} (check your config)"
    response_json = response.json()
    repositories = []
    for repo_name in response_json.get("repositories", []):
        tags_response = requests.get(f"{registry.url}/{registry.version}/{repo_name}/tags/list")
        tags_json = tags_response.json().get("tags", [])
        tags = []
        for tag_name in tags_json:
            manifest_response = requests.get(f"{registry.url}/{registry.version}/{repo_name}/manifests/{tag_name}")
            manifest_json = manifest_response.json()
            tag = {
                "name": tag_name,
                "manifest": manifest_json,
            }
            tags.append(tag)
        repo = {
            "name": repo_name,
            "tags": tags,
        }
        repositories.append(repo)

    ctx = {
        "registry": registry,
        "repositories": repositories,
    }
    return render_template("browse.html", ctx=ctx, **ctx)
