import requests
import os
from pyfzf import FzfPrompt
import json
query = input('enter search term : ')
query = query.replace(' ', '+')
url = f'https://me0xn4hy3i.execute-api.us-east-1.amazonaws.com/staging/api/resolve/resolveYoutubeSearch?search={query}'
sess = requests.Session()
resp = sess.get(url)
data = json.loads(resp.text)
vids = data['data']
links = {}
for vid in vids:
    links.update({vid['title']:vid['url']})
fzf = FzfPrompt()
selected = fzf.prompt(links.keys())[0]
os.system(f'youtube-dl -f bestaudio "{links.get(selected)}"')
