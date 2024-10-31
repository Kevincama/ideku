# Pre-condition:
```
- python3.11
- pipenv (pip3 install pipenv)
```
### Requirements
```
- pipenv install
```
### Execute steps:
```
- pipenv shell
- pytest -v -s tests/login_flow -> Execute the tests under folders
- pytest -v -s tests/login_flow -m p0 -> Execute the tests with specific mark
```

### Structure:
- **config/**
  - Store the info that will be use when testing, and change less. Ex. browserName
- **pages/**
  - Define all pages element or function
- **testdata/**
  - Store testdata, inculde test env and prod env 
- **tests/**
  - The test steps
- **utility/**
  - Can help the test execute

### Note:
- Using pytest + selenium to complete
- The better way may be using the docker image from selenium hub
  - https://hub.docker.com/r/selenium/hub
- Should design with CI/CD tools, so I'm not write docker flow in this file, just introduce.

------

## About pytest.ini

- Can define like mark or others that will let pytest run more efficiently




