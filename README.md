## drone step
```yaml
---
kind: pipeline
type: docker

# # This is optinoal
# clone:
#   disable: true

steps:
  - name: clone trigger drone build repo
    image: drone/git
    commands:
      - git clone https://github.com/CardioController/trigger-drone-build.git trigger-drone-build

  - name: trigger build
    image: python:alpine
    environment:
      DRONE_SERVER: 
        from_secret: DRONE_SERVER
      DRONE_TOKEN:
        from_secret: DRONE_TOKEN
      REPO_OWNER: 
        from_secret: REPO_OWNER
      REPO_NAME:
        from_secret: REPO_NAME
    commands:
      - cd trigger-drone-build
      - pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple drone-python
      - pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple urllib3 --upgrade
      - python main.py
      - echo "Goto ${DRONE_SERVER}/${REPO_OWNER}/${REPO_NAME} to see build status"
```

## environment variables
```
DRONE_SERVER
DRONE_TOKEN
REPO_OWNER
REPO_NAME
```