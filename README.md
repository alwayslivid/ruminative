# RUMINATIVE

A simple reconnaissance tool utilizing Shodan. [![Build Status](https://travis-ci.org/alwayslivid/ruminative.svg?branch=master)](https://travis-ci.org/alwayslivid/ruminative)

**Usage**

* Add your Shodan token in the `secret.py` file.
* Alternatively, add your Shodan token in an environment variable with the key `SHODAN_KEY`. The tool prioritizes the `SHODAN_KEY` environment variable over the `secret.py` file.
* Alternatively, enter your Shodan token in the terminal as an argument. Or, just don't do anything and the script is going to ask you whether you want to add a token.
* Shodan will return results matching your public IP address. 

**Requirements**

* Python 3
* [Shodan](https://pypi.python.org/simple/shodan/)
* Access to [Shodan](https://shodan.io), as well as the API key corresponding to your account.
* Access to the target network with unfiltered internet access.