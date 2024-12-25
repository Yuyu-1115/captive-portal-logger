import requests
import keyring

# using HTTP so the captive portal can intercept with the connection
test_link = "http://captive.apple.com/"
prefix = "auto-logger:"

response = requests.get(test_link, allow_redirects=True)
if response.status_code != 200:
    response.raise_for_status()
if response.url != test_link:
    print(prefix, "Redirected to ", response.url)
else:
    print(prefix, "Fail to redirect to the captive portal, please check the network connection")
