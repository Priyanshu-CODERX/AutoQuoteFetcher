# Fetch Quotes from Quotables Database ~ Done
# Automate The Quote ~ Done

import requests
import time

def getQuotes(): # Fetching the quotes from Quotable's Database
	response = requests.get('https://api.quotable.io/random')
	if response.status_code == 200:
		quotes = response.json()
		quote = 'f{quotes[content]})'
		print(quotes)
	else:
		print("Failed to get a quote")

def main():
	try:
		while True: # Automating the code
			getQuotes()
			time.sleep(5)
	except KeyboardInterrupt:
		print("Thank You! Quitting")
	except Exception as e:
		pass


if __name__ == '__main__':
	main()
