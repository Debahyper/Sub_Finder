
import requests
import pyfiglet


ascii_banner = pyfiglet.figlet_format("SUB FINDER.1")
print(ascii_banner)
print('                                                                 ----with Deba.V1')


domain = input("Enter domain: ")
file = open('subdomain.txt','r')
content = file.read()

subdomains = content.splitlines()
for subdomain in subdomains:
	url1 = f"http://{subdomain}.{domain}"
	url2 = f"https://{subdomain}.{domain}"
	try:
		requests.get(url1)
		print(f"Discovered URL: {url1}")
		requests.get(url2)
		print(f"Discovered URL: {url2}")
	except requests.ConnectionError:
		pass