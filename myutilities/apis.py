from myutilities import secret
import requests

def test_response(site):
	one_secret = secret.print_headers()[site]
	header = one_secret['Authorization']
	url = str(one_secret['url'])
	response = requests.get(url=url, headers=header)
	return print(header)

def main():
	test_response('github')
	pass

if __name__ == '__main__':
	response = requests.get("https://api.github.com/users/VikParuchuri/orgs", headers=headers)
	orgs = response.json()


