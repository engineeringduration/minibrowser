import requests
import time


# URL to scrape
url = "https://www.flipkart.com/pens-stationery/pr?sid=dgv&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&hpid=B2Ku1G4aX7ZGf37AOgCozap7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTQ5Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fSwiaGVyb1BpZCI6eyJzaW5nbGVWYWx1ZUF0dHJpYnV0ZSI6eyJrZXkiOiJoZXJvUGlkIiwiaW5mZXJlbmNlVHlwZSI6IlBJRCIsInZhbHVlIjoiREtPR1lURU1OU1pZUktLSiIsInZhbHVlVHlwZSI6IlNJTkdMRV9WQUxVRUQifX0sInRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlRvcCBTZWxsaW5nIFN0YXRpb25lcnkiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19"

# Headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://www.google.com"
}

# Proxy authentication
proxy_auth = "username:password@proxyserver.com:port"
proxies = {
    "http": f"http://{proxy_auth}",
    "https": f"https://{proxy_auth}"
}

# Create a session
session = requests.Session()

# Sleep to avoid detection (optional)
time.sleep(2)

try:
    # Send GET request with proxies and headers
    response = session.get(url, proxies=proxies, headers=headers)
    
    # Save the HTML content
    with open("output.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    print("Webpage saved successfully!")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
