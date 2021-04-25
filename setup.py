from setuptools import setup
setup(
    name='Patbot',
    version='1.0',
    description='Pat discord bot',
    author='Will Schmidt',
    author_email='schmidt.will9@gmail.com',
    packages = ['Patbot'],
    install_requires=['os','discord','dotenv','random','requests'])