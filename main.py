import os
from drone import drone

REPO_OWNER = os.environ['REPO_OWNER']
REPO_NAME = os.environ['REPO_NAME']

if __name__ == '__main__':
    repo = drone(REPO_OWNER, REPO_NAME)
    latest_build = repo.build.all()[0]
    repo.build.restart(latest_build['number'])
    pass

