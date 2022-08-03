#!/usr/bin/env python3

import sys
import os
import datetime as dt
from github import Github

print("GH_TOKEN: ", os.environ.get("GHI_TOKEN"))
github_token = sys.argv[1]
new_files = sys.argv[2:]



g = Github(github_token)
for repo in g.get_user().get_repos():
    print(repo.name)

matchers = {
    # "src/ezer": "ezer.test",
    # "src/nada/app": "nada.test",
    #  "src/nada/utils/lambda": "lambda-produce.test",
    "app": "lambda-deploy.test",
    ".github/": "github",
    "selector": "wow",
    #  "src/infra/aws/workload/nada": "infra-nada.test",
    #  "src/infra/aws/management/dns": "dns.test",
    #  "src/infra/aws/management/stacksets": "stacksets.test",
}

ts = dt.datetime.now().strftime('%Y-%m-%dT%H%M%S')

tags = set()
for f in new_files:
    for m in matchers:
        if f.startswith(m):
            tags.add(matchers[m])

tags = list(map(lambda m: f"{m}@{ts}", tags))
print(f"tags: {tags}")

with open('tags.txt', 'w') as f:
    f.write("\n".join(tags))

# import os
# for tag in tags:
#     os.system(f'git tag {tag}')
#     os.system(f'git push origin {tag}')
import os

os.environ.get("")

first_commit = repo.revparse_single("HEAD")
tagger = pygit2.Signature("github CI", "noreply@carbonre.tech")
for tag in tags:
    print("(tag, first_commit.oid.hex, pygit2.GIT_OBJ_COMMIT, tagger)",
          (tag, first_commit.oid.hex, pygit2.GIT_OBJ_COMMIT, tagger, ""))
    print(repo.create_tag(tag, first_commit.oid.hex, pygit2.GIT_OBJ_COMMIT, tagger, ""))

ori_remote = repo.remotes[0]
userName = "gunkow"
# credentials = pygit2.UserPass(userName, password)
credentials = pygit2.Keypair(userName, "~/.ssh/id_rsa.pub", "~/.ssh/id_rsa", "")
# credentials = pygit2.KeypairFromMemory(userName, str(Path('~/.ssh/id_rsa.pub').expanduser().read_text()), str(Path('~/.ssh/id_rsa').expanduser().read_text()), "")

ori_remote.credentials = credentials
callbacks = pygit2.RemoteCallbacks(credentials=credentials)
ori_remote.push(["refs/heads/master"], callbacks=callbacks)
