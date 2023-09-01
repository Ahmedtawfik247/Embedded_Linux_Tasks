import requests

def get_public_ip():
  """Gets the public IP address of the machine."""
  url = "https://api.ipify.org/?format=json"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()["ip"]
  else:
    raise Exception("Could not get public IP address.")


if __name__ == "__main__":
  public_ip = get_public_ip()
  print(public_ip)