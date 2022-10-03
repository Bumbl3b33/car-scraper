# Car Scarper - Web Scraping Tool for Riyasewana.lk

This tool can be used to log data about cars for future reference and track prices of wanted models

## Initial Setup

- Create a virtual environment `python -m venv <name-of-venv>`
- Download the webdriver. For Edge -> <https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/>
- Place the webdriver file in the same folder as the `.py` file
- Install the dependencies in requirements.txt using `pip install -r requirements.txt`

## Usage

- Enter the search terms to be scraped into `toScrape.txt`
- Run the program (main.py)
- After the program exits, check the `logs` folder to view the generated scraped data
