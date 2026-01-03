import requests

requests.packages.urllib3.disable_warnings()

HEADERS = {
    "User-Agent": "VulnScanner/1.0"
}

def send(url, method="GET", params=None):
    try:
        r = requests.request(
            method,
            url,
            headers=HEADERS,
            params=params,
            timeout=8,
            verify=False
        )
        return r
    except requests.RequestException:
        return None
