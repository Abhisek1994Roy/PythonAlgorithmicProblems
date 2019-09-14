# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# This file is licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License. A copy of the
# License is located at
#
# http://aws.amazon.com/apache2.0/
#
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import boto3
import sys
import json

file_name = sys.argv[1]


# get the results
client = boto3.client(
         service_name='textract',
         region_name= 'us-east-1',
         endpoint_url='https://textract.us-east-1.amazonaws.com',
         aws_access_key_id='AKIA6EPTKPHRRWBK6J4I',
         aws_secret_access_key='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',

)


def get_kv_map(file_name):

    with open(file_name, 'rb') as file:
        img_test = file.read()
        bytes_test = bytearray(img_test)
        print('Image loaded', file_name)

    # process using image bytes
    response = client.analyze_document(Document={'Bytes': bytes_test}, FeatureTypes=['FORMS'])

    # Get the text blocks
    blocks=response['Blocks']
    with open("textract3.json", "w") as outfile:
        json.dump(response, outfile, indent=4)

    lineArr = []
    wordArr = []

    for block in blocks:
        if block["BlockType"] == "LINE":
            lineArr.append(block["Text"])
        if block["BlockType"] == "WORD":
            wordArr.append(block["Text"])

    print(lineArr)
    print("-------------")
    print(wordArr)


file = "https://ksf-raw-data-dev.s3.ap-south-1.amazonaws.com/Test_Image.jpeg"
# MAIN PROGRAM
get_kv_map(file_name)




