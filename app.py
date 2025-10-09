from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        verify_token = 'brian-bot-token'
        if request.args.get('hub.verify_token') == verify_token:
            return request.args.get('hub.challenge')
        return 'Invalid token'

    elif request.method == 'POST':
<<<<<<< HEAD
        try:
            data = request.json
            message = data['entry'][0]['changes'][0]['value']['messages'][0]
            text = message['text']['body'].strip().lower()
            sender = message['from']

            print(f"📩 Incoming message from {sender}: {text}")  # ✅ Logging

            # ✅ Command variations
            if any(keyword in text for keyword in ["registration sheet", "get sheet", "show registration"]):
                sheet_url = 'https://script.google.com/macros/s/AKfycbwLLx_fNpwz3GRv8NgN8jReC9ge899jW0fS87kaHdaKlqrBjnsrPcbYIVNrdDE-fBuWEg/exec'
                try:
                    sheet_data = requests.get(sheet_url).json()
                    reply = "📋 Registration Sheet:\n"
                    for entry in sheet_data[-5:]:
                        reply += f"- {entry.get('Name', 'N/A')} | {entry.get('Phone', 'N/A')} | {entry.get('Email', 'N/A')}\n"
                except Exception as e:
                    print(f"❌ Error fetching sheet: {e}")
                    reply = "⚠️ Sorry, I couldn't fetch the registration sheet right now."

                send_whatsapp_message(sender, reply)

            else:
                send_whatsapp_message(sender, "🤖 Hi! To get the latest registration sheet, type: *Registration Sheet*, *Get Sheet*, or *Show Registration*")

        except Exception as e:
            print(f"❌ Malformed payload: {e}")
            return 'Malformed payload', 400

        return 'OK'


def send_whatsapp_message(to, message):
    url = "https://graph.facebook.com/v19.0/8626968538561715/messages"
    headers = {
        "Authorization": "Bearer EAAVPkFwL6B0BPhReC1Ivj8FZAZBmsBk3xJlKZCT2JrKPJAKVJZANwEeOwaPsA73trF16kV9ZBLXWnx1GuGLHBSD92SszzVBXfMfHunrjD7ZBqA83Ackeet1B5oJayiug4mO6FgV3Bas0TTO0j00DMrTtn3ePy4LoN8ZBnDgR8Va6XwwRBGr1quZBJmZBDpFSZBTV6A3pOgoNNl6hqoIt0DM9rXtZCPbWiO82IZAvmaXMmhZCzpYik2QZDZD",
=======
        data = request.json
        message = data['entry'][0]['changes'][0]['value']['messages'][0]
        text = message['text']['body'].strip().lower()
        sender = message['from']

        if "registration sheet" in text:
            sheet_url = 'https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec'  # Replace with your actual Google Apps Script URL
            sheet_data = requests.get(sheet_url).json()

            reply = "📋 Registration Sheet:\n"
            for entry in sheet_data[-5:]:  # last 5 entries
                reply += f"- {entry['Name']} | {entry['Phone']} | {entry['Email']}\n"

            send_whatsapp_message(sender, reply)

        return 'OK'

def send_whatsapp_message(to, message):
    url = "https://graph.facebook.com/v19.0/YOUR_PHONE_NUMBER_ID/messages"  # Replace with your actual Phone Number ID
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",  # Replace with your temporary access token
>>>>>>> e228ea15b0ad95e6a765ea179b13b031584eb1f6
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message}
    }
<<<<<<< HEAD
    response = requests.post(url, headers=headers, json=payload)
    print(f"📤 WhatsApp API response: {response.status_code} - {response.text}")  # ✅ Delivery logging
=======
    requests.post(url, headers=headers, json=payload)
>>>>>>> e228ea15b0ad95e6a765ea179b13b031584eb1f6
