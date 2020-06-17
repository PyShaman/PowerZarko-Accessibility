# PowerZarko Accessibility 
_User guide_


**List of contents**

**1. Python version and installation**

**2. Installing required packages and tools**

**3. Usage**

**4. Output**


_1. Python version and installation_

Tests are written in Python 3.8+ and it should be ran on this version or higher.
User can download newest version of Python at [Python download site](https://www.python.org/downloads/).

Install [PIP](https://pypi.org/project/pip/).

_2. Installing required packages and tools_

After cloning [PowerZarko Accessibility](https://github.com/PyShaman/PowerZarko-Accessibility) repository locally user should enter folder and create separate virtual environment for this project by using following command:
```
$ python -m venv venv
```
Python will create new directory called venv and install there basic packages. Next step is to activate virtual environment:
```
$ ./venv/Scripts/Activate.ps1
```
for Windows systems or
```
$ ./venv/Scripts/activate
```
for Linux.
When virtual environment will be activated the user will see additional mark at console:
```
(venv) path\PowerZarko-Accessibility >
```
Next step is to install required packages using following command:
```
$ pip3 install -r requirements.txt
```

This will automatically download and install all necessary packages.
Next very important step is to manually update axe-python-selenium package with newest accessibility script. To do so,
check the version of current axe.min.js file in main directory (axe v3.5.3). Then visit [this](https://github.com/dequelabs/axe-core-maven-html/blob/develop/src/test/resources/axe.min.js)
 site and check current version. If it differs, download newer one. Next step is to copy axe.min.js to following directory:
```
\venv\Lib\site-packages\axe_selenium_python\node_modules\axe-core\
```
At the end fill the list of url to scan in sites.py file.

After this operation you are ready to go and you can scan websites against accessibility :)

_3. Usage:_

To run all tests use following command:
```
$ python test_01_accessibility_wcag2a.py
```

_4. Output:_

The tests will perform WCAG 2A, WCAG 2AA, full accessibility scan and finally vulnerability scan of the websites.
Results of accessibility will be kept in results folder.

