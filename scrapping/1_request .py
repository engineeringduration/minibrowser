from requests_html import HTMLSession
session = HTMLSession()
r= session.get('https://python.org/')

print(r.html.links)

about = r.html.find('#about', first=True)

print(about)
print(about.text)


