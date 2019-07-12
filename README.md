# Selenium
Browser automation code

## Getting Started


### Prerequisites
 
```
Python
Firefox
geckodriver
php server
php-webdriver (for php scripts)
selenium server (optional for remote execution)
```

### Installing

```
pip install selenium
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar xzvf geckodriver-v0.24.0-linux64.tar.gz
mv geckodriver /usr/bin/
wget https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar
```
for a remote server:
```
java -jar selenium-server-standalone-3.141.59.jar &
```
or (was having problems with php codes executing above v3.8.1)
```
java -jar selenium-server-standalone-3.8.1.jar -enablePassThrough false &
```

### Running the tests

```
python script.py
```

## For more detailed information visit Seleniumhq.org
