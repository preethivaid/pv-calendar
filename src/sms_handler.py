







from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from src.calendar_handler import CalendarHandler
from src.sheets_handler import SheetsHandler
from src.utils import format_message

app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    sms_request = request.form['Body']
    sms_response = MessagingResponse()

    SheetsHandler().call_sheets()


    # if request.form['From'] == '+18604024490':
    #     if "summary" in sms_request.split(" ")[0].lower():
    #         calendar_summary_text = CalendarHandler().get_summary(sms_request)
    #         sms_response.message(calendar_summary_text)
    #     elif "delete" in sms_request.split(" ")[0].lower():
    #         calendar_summary_text = CalendarHandler().delete_event(sms_request)
    #         sms_response.message(calendar_summary_text)
    #     else:
    #         response_text = CalendarHandler().create_event(sms_request)
    #         sms_response.message(response_text)
    # else:
    #     sms_response.message(format_message('Nice try buddy!'))
    return str(sms_response)


def run():
    app.run()

if __name__=="__main__":
    run()