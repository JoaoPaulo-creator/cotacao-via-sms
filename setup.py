from setuptools import setup

setup(
    name='cotaca-via-sms',
    version='0.1.0',
    description='',

    install_requires=['anyio',
                      'httpcore',
                      'httpx',
                      'idna',
                      'py',
                      'pytest',
                      'twilio',
                      'urllib3'],

    classifiers=['Programming Language :: Python',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.10', ],

    author='Joao',
    author_email='joaosarto@gmail.com',
    url='https://github.com/JoaoPaulo-creator/cotacao-via-sms'
)
