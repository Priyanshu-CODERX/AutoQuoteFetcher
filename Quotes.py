# Fetch Quotes from Quotables Database ~ Done
# Automate The Quote ~ Done

import requests
import time

def getQuotes(): # Fetching the quotes from Quotable's Database
	url = 'https://api.quotable.io/random'
	parameters = {'content' : 'famous-quotes'}
	response = requests.get(url, params=parameters)
	if response.status_code == 200:
		quotes = response.json()
		print(quotes['content'])
		print(quotes['author'])
	else:
		print("Sorry! Cannot get you a quote right now :( Please try again after sometime")

def main():
	try:
		while True: # Automating the code
			getQuotes()
			print('__________________________________________________________')
			print()
			time.sleep(5)
	except KeyboardInterrupt:
		print("Thank You! Quitting")
	except Exception as e:
		pass


if __name__ == '__main__':
	main()
