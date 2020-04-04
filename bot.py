    # Spam the phishers!

    # Made by deyyanl
    # Use it however you want :)

    # v0.0.1

import os
import requests
import string
import random
import json
from lxml.html import fromstring
from itertools import cycle
import traceback

# Random characters
ch = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

# URL of the scammer
phisher_url = 'https://glthubs.info/attempts.php'

# File path of name list
names = json.loads(open('names.json').read())

# Define function to get fresh proxies
def getProxiesList():
    # URL with free proxies
    proxy_url = 'https://free-proxy-list.net'
    # Get the response from the page
    proxy_response = requests.get(proxy_url)
    # Parse the response
    parser = fromstring(response.text)
    proxies = set()
    # Get proxies from page's body using XPATH via webdriver
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            # One specific proxy from the list
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            # Add proxy to the set 
            proxies.add(proxy)
    return proxies

fetchedProxies = getProxiesList()
# Cycle through the fetched proxies
proxy_pool = cycle(fetchedProxies)

for name in names:
    # Get proxy
    proxy_to_use = next(proxy_pool)
	# Extra string the name using random generation
    name_extra = ''.join(random.choice(string.digits))

    # Generate fake username
	username = name.lower() + name_extra + '@yahoo.com'
	# Generate fake password
    password = ''.join(random.choice(chars) for i in range(8))

    try: 
        # Send the request
        # NOTE: If your site uses GET method, change the code to be compatible with it
        requests.post(phisher_url,proxies={"http": proxy_to_use, "https": proxy_to_use}, allow_redirects=False, data={
            # Form data for username (change the names accordingly to your site)
            'user': username,
            # Form data for password
            'pass': password
            # Additional form data
            # 'try': true
        })
    except: 
        print("Skipping the proxy. Connection error")
    

	print 'Spamming with: UN: %s and PASS: %s' % (username, password)