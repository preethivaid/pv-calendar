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
        sms_response.message('Here is the summary for that day: {}'.format(calendar_summary_text))
    else:
        CalendarHandler().create_event(sms_request)
        sms_response.message('Added {} to calendar!'.format(sms_request))
    return str(sms_response)


if __name__ == '__main__':
    app.run()
