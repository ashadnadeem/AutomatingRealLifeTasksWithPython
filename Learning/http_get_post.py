__author__ = "Ashad Nadeem Mahmudi"
__date__ = "9/4/2020"

import requests

url = "https://www.google.com.pk"

response = requests.get(url)
if not response.ok:
    print(response.status_code)

#Html content
print(response.content)