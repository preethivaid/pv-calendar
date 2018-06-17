import xmltodict
import argparse
from src.sms_handler import cal_app
testapp = cal_app.test_client()


class FakeSms:

    @staticmethod
    def fake_sms(args):
        response = testapp.post(
            '/sms',
            data=dict(Body=args.sms_body,
                      From=args.phone_number))
        print("======")
        print((response.data))
        print("======")
        parsed_response = xmltodict.parse(response.data)["Response"]["Message"]
        print(parsed_response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('sms_body', action='store',
                        help='The body of the sms')
    parser.add_argument('-n', action='store', dest='phone_number', default="+18604024490",
                        help='The phone number of the sms')
    args = parser.parse_args()
    FakeSms().fake_sms(args)
