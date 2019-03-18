# RUMINATIVE
[![Build Status](https://travis-ci.org/alwayslivid/ruminative.svg?branch=master)](https://travis-ci.org/alwayslivid/ruminative)

A simple reconnaissance tool utilizing Shodan. 

## Getting started

* Add your Shodan token in the `secret.py` file.
* Alternatively, add your Shodan token in an environment variable with the key `SHODAN_KEY`. The tool prioritizes the `SHODAN_KEY` environment variable over the `secret.py` file.
* Alternatively, enter your Shodan token in the terminal as an argument. Or, just don't do anything and the script is going to ask you whether you want to add a token.
* Shodan will return results that match your external IP address.

Please note that this tool works well in places that are open to the public or .

## Prerequisites

* Python 3
* [Shodan's Python library.](https://pypi.python.org/simple/shodan/)
* Access to [Shodan](https://shodan.io), as well as the API key corresponding to your account.
* Unfiltered internet access within the target network.

## Authors

* **Panos V.** - *Initial work.* - [AlwaysLivid](https://alwayslivid.com)

## Acknowledgements

This tool was inspired by the following open-source projects:

* [Shodan Mattermost](https://github.com/PaulSec/Shodan-mattermost) *by [PaulSec](https://github.com/PaulSec)*

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details