from flask import Flask, request
from pymessenger.bot import Bot

app = Flask("hello")

VERIFY_TOKEN = '1234567890'
ACCESS_TOKEN = 'EAADynbXTAgoBAERa2F0tXZBhK60PUbpEyb0fFuZCyxiDvGlsXIcFJwSMTYoYfPIO60CxOsWY85rFJmfkjuZC5eNPiwpZC0OAeoj6KTRBhPsS9Kq9zQZAL4jDDKkqEcbYAfoeCPI9ZATkRZAHtWXxB8LoTb9osLkieKh8Pkfmkl246uCgWu4CFmC '

pybot = Bot(ACCESS_TOKEN)


@app.route("/check/", methods=['get'])
def hi():
    return "Working"


@app.route("/callback/", methods=['GET'])
def get_callback():
    if VERIFY_TOKEN == request.args.get("hub.verify_token"):
        return request.args.get("hub.challenge")
    else:
        return "Not Working"


@app.route("/callback/", methods=['POST'])
def post_callback():
    output = request.get_json()
    print(output)
    for entry in output.get("entry"):
        if "messaging" in entry:
            for messaging in entry.get("messaging"):
                sender = messaging.get("sender").get("id")
                recipient = messaging.get("recipient").get("id")
                text = 'You Sent an Attachment'
                if "text" in messaging.get("message"):
                    text = messaging.get("message").get("text")

                print(sender, recipient, text)
                pybot.send_text_message(sender, text)
                pybot.send_image_url(sender, r"https://image.shutterstock.com/image-vector/welcome-vector-lettering-on-blurred-260nw-736049245.jpg")
    return "done"


app.run()

# Web hook and callback are sme concept
