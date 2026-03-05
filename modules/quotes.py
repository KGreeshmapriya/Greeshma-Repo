import requests

def get_quote():

    url = "https://api.quotify.top/random"
    try:
        r = requests.get(url, verify=False).json()
        return r["content"]

    except:
        return "Stay positive and keep building projects!"