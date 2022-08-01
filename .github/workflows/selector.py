#!/usr/bin/env python3

import datetime as dt
from os.path import dirname
from pygit2 import Repository

repo = Repository('.git')

dirs = set()

def add_dir(p):
    if p and p not in dirs:
        dirs.add(p)
        add_dir(dirname(p))

for p in repo.diff('HEAD', 'HEAD^'):
    add_dir(dirname(p.delta.new_file.path))
    add_dir(dirname(p.delta.old_file.path))

matchers = {
    #"src/ezer": "ezer.test",
   # "src/nada/app": "nada.test",
  #  "src/nada/utils/lambda": "lambda-produce.test",
    "src/dashboard": "lambda-deploy.test",
  #  "src/infra/aws/workload/nada": "infra-nada.test",
  #  "src/infra/aws/management/dns": "dns.test",
  #  "src/infra/aws/management/stacksets": "stacksets.test",
}


ts = dt.datetime.now().strftime('%Y-%m-%dT%H%M%S')

for d in dirs:
    if d in matchers:
        print(matchers[d])
        print(f"{matchers[d]}@{ts}")