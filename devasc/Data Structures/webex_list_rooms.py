import requests

url = "https://webexapis.com/v1/rooms?sortBy=lastactivity"

payload = ""
headers = {
  'Authorization': 'Bearer OWUzZTE0MTAtYWVlZC00OWI2LWIxZTAtYzY2NWQwNTQzYmU2Y2EwYWUwZmYtMjMx_P0A1_94fa23f6-cfc1-441d-85e3-97d0e72a2d7e',
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False).json()

print(response)


