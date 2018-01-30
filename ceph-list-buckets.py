#! /usr/bin/env python3


import os
import sys
import json

import boto3


with open('credentials.json', 'r') as fd:
    credentials = json.loads(fd.read())


def main():

    s3 = boto3.client('s3',
                      endpoint_url=credentials['endpoint_url'],
                      aws_access_key_id=credentials['access_key'],
                      aws_secret_access_key=credentials['secret_key'])

    response = s3.list_buckets()
    for item in response['Buckets']:
        print(item['CreationDate'], item['Name'])


if __name__ == '__main__':
    main()
