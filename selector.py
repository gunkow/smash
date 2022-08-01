#!/usr/bin/env python3

import sys
import datetime as dt
import pygit2

repo = pygit2.Repository('.git')

new_files = sys.argv[1:]


matchers = {
    #"src/ezer": "ezer.test",
   # "src/nada/app": "nada.test",
  #  "src/nada/utils/lambda": "lambda-produce.test",
    "app": "lambda-deploy.test",
    ".github/": "wow"
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

tags = map(lambda m: f"{m}@{ts}", matchers)

first_commit = repo.revparse_single("HEAD")
tagger = pygit2.Signature("github CI", "noreply@carbonre.tech")


for tag in tags:
  print("(tag, first_commit.oid.hex, pygit2.GIT_OBJ_COMMIT, tagger)", (tag, first_commit.oid.hex, pygit2.GIT_OBJ_COMMIT, tagger, ""))
  print(repo.create_tag(tag, first_commit.oid.hex, pygit2.GIT_OBJ_COMMIT, tagger, ""))

print(list(tags))