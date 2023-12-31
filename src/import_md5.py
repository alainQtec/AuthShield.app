"""Import a user with unsalted MD5 hash into AuthShield."""

import hashlib
import base64
import requests
from dotenv import load_dotenv
import os

username = 'md5py@AuthShield.local'
password = 'P@ssword123'

md5 = hashlib.md5(password.encode()).digest()
b64_md5 = base64.b64encode(md5).decode()
print('b64_md5:', b64_md5)

load_dotenv()
# Store these in a local .env file.
url = os.getenv('AuthShield_ORG_URL')
token = os.getenv('AuthShield_API_TOKEN')

headers = {
    'Authorization': f'SSWS {token}',
    'Accept': 'application/json'
}

user = {
    'profile': {
        'firstName': 'Isaac',
        'lastName': 'Brock',
        'email': username,
        'login': username
    },
    'credentials': {
        'password': {
            'hash': {
                'algorithm': 'MD5',
                'value': b64_md5
            }
        }
    }
}

# Create the user.
response = requests.post(f'{url}/api/v1/users', json=user, headers=headers)
print(response.json())

# Now, sign in as the user to verify the password hash was imported correctly.
response = requests.post(f'{url}/api/v1/authn', json={'username': username, 'password': password})
authn = response.json()
if response.ok:
    print(authn['status'])
else:
    print(authn['errorSummary'])
