from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from src.calendar_handler import CalendarHandler

app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    sms_request = request.form['Body']
    sms_response = MessagingResponse()
    if "summary" in sms_request.split(" ")[0].lower():
        calendar_summary_text = CalendarHandler().get_summary(sms_request)
        sms_response.message(calendar_summary_text)
    else:
        response_text = CalendarHandler().create_event(sms_request)
        sms_response.message(response_text)
    return str(sms_response)


def run():
    app.run()
