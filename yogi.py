import requests

url = 'https://hooks.slack.com/services/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'
myobj = {"text": "This is posted to #general and comes from a bot named webhookbot.", "icon_emoji": ":ghost:"}

x = requests.post(url, json = myobj)


print(x.text)
