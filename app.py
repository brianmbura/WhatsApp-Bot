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
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message}
    }
    requests.post(url, headers=headers, json=payload)
