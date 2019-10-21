# from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='pv-calendar',
    version='0.0.0',
    packages=find_packages(),
    url='',
    license='',
    author='Preethi Vaidyanathan',
    author_email='preethivaid@gmail.com',
    description='A sms to google calendar interface to help Preethi Vaidyanathan remember things.',
    install_requires=[
        'cachetools==2.1.0',
        'certifi==2018.4.16',
        'chardet==3.0.4',
        'click==6.7',
        'DateTime==4.2',
        'dateparser==0.7.0',
        'Flask==1.0.2',
        'google-api-python-client==1.7.1',
        'google-auth==1.5.0',
        'google-auth-httplib2==0.0.3',
        'gunicorn==19.8.1',
        'httplib2==0.11.3',
        'idna==2.6',
        'itsdangerous==0.24',
        'Jinja2==2.10',
        'MarkupSafe==1.0',
        'oauth2client==4.1.2',
        'pyasn1==0.4.3',
        'pyasn1-modules==0.2.1',
        'PyJWT==1.6.4',
        'PySocks==1.6.8',
        'python-dotenv==0.8.2',
        'pytz==2018.4',
        'requests==2.18.4',
        'rsa==3.4.2',
        'six==1.11.0',
        'twilio==6.14.3',
        'uritemplate==3.0.0',
        'urllib3==1.22',
        'Werkzeug==0.15.3'],
)
