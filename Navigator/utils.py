import requests
import json
from operator import itemgetter
import re
from time import strftime

REPO_SEARCH_URL = "https://api.github.com/search/repositories?q={0}+in:name"


def get_repositories(search_term, page_size, order):
    r = requests.get(REPO_SEARCH_URL.format(search_term), proxies={'http': "proxy.uk.labs.sophos:8080", 'https': "proxy.uk.labs.sophos:8080"}) #Remove proxies
    content = json.loads(r.content.decode(encoding="utf-8"))

    refined_repos = []
    if content["items"]:
        for item in content["items"]:
            if search_term in item["name"]:
                refined_repos.append(refine_results(item))

        refined_repos = sorted(refined_repos, key=itemgetter("created_at"), reverse=order)[:min(page_size, len(refined_repos))]
        add_commit_details(refined_repos)
        return refined_repos
    else:
        return


def add_commit_details(refined_repos):
    for refined_repo in refined_repos:
        commits_url = re.sub(r"{/sha}", r"/master", refined_repo["commits_url"])
        r = requests.get(commits_url, proxies={'http': "proxy.uk.labs.sophos:8080", 'https': "proxy.uk.labs.sophos:8080"})
        content = json.loads(r.content.decode(encoding="utf-8"))
        del refined_repo["commits_url"]
        refined_repo.update({'last_commit_sha': content['sha'], 'last_commit_message': content["commit"]["message"],
                             'last_commit_author_name': content["commit"]["author"]["name"]})


def refine_results(repo_details):
    keys = ["name", "created_at", "avatar_url", "", "commits_url"]
    filtered_dict = {k:v for k, v in repo_details.items() if k in keys}
    filtered_dict['created_at'] = strftime("%Y-%m-%d %H:%M:%S")
    filtered_dict["login_url"] = repo_details["owner"]["html_url"]
    filtered_dict["login_name"] = repo_details["owner"]["login"]
    filtered_dict["avatar_url"] = repo_details["owner"]["avatar_url"]
    return filtered_dict
