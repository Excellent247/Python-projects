# Project algorithm

# 1. request module
# 2. API (url) for pull request
# 3. convert JSON to Dictionary
# 4. print result.

import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

pr_info=response.json()
for i in range(len(pr_info)):
    print(pr_info[i]["user"]["login"])
