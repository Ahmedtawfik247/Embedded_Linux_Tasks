#----------------------------------------
#code to find bitcoin rate automatically.
#----------------------------------------
import requests

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(response.json()['bpi']['USD'])
