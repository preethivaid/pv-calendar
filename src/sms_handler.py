from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from src.create_event import CreateEvent

app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    event_summary = request.form['Body']

    CreateEvent.create_event(event_summary)

    resp = MessagingResponse()
    resp.message('Added {} to calendar!'.format(event_summary))
    return str(resp)


if __name__ == '__main__':
    app.run()
