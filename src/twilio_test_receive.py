from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from src.create_event import CreateEvent

app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    message_body = request.form['Body']

    CreateEvent.create_event(message_body)

    resp = MessagingResponse()
    resp.message('Added {} to calendar!'.format(message_body))
    return str(resp)


if __name__ == '__main__':
    app.run()