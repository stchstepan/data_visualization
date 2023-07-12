import requests

class Api():
    def __init__(self, url='https://api.github.com/search/repositories?q=language:python&sort=stars', 
              headers={'Accept': 'application/vnd.github+json'}):
        self.url = url
        self.headers = headers

    def check_api(self):
        r = requests.get(self.url, headers=self.headers) 
        return r.status_code
    
    def len_repo_dicts(self):
        response_dict = requests.get(self.url, headers=self.headers).json()
        return response_dict['total_count']