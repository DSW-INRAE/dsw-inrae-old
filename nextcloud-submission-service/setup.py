from setuptools import setup, find_packages
import os

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = ''.join(f.readlines())

setup(
    name='nextcloud_submitter',
    version='1.0.0',
    keywords='dsw submission document nextcloud',
    description='This submissions service will allow you to directly submit documents in a NextCloud instance',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Théodore Picot',
    author_email='theodorebjpicot@gmail.com',
    license='Apache2',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'PyYAML',
        'requests',
        'uvicorn[standard]',
    ],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
    ],
)
