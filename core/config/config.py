import os
import yaml

conf_path = os.path.join(os.path.dirname(__file__), 'config.yml')
data = yaml.safe_load(open(conf_path, 'r'))

class Config:

    def __init__(self):
        self.consumerkey = data.get('keys').get('consumer_key')
        self.consumerkey_secret = data.get('keys').get('consumer_secret')
        self.accesstoken = data.get('keys').get('access_token')
        self.accesstoken_secret = data.get('keys').get('access_token_secret')

if __name__ == "__main__":
    c = Config()
    print(c.accesstoken)