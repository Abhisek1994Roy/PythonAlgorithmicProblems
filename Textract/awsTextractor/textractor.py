import os
import sys
import boto3
import json
from google.cloud import vision
from google.cloud.vision import types


client = vision.ImageAnnotatorClient()

dir_name = sys.argv[1]


# create a boto3 client for aws services
# client = boto3.client(
#          service_name='textract',
#          region_name= 'us-east-1',
#          endpoint_url='https://textract.us-east-1.amazonaws.com',
#          aws_access_key_id='AKIA6EPTKPHRRWBK6J4I',
#          aws_secret_access_key='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',
#
# )



def extract_details(dirName):
    for fileName in os.listdir(dirName):
        if fileName.endswith(".jpg") or fileName.endswith(".png") or fileName.endswith(".jpeg"):
            # createConsumable(os.path.join(dirName, fileName))
            cloudVision(os.path.join(dirName, fileName),fileName)
            continue
        else:
            continue
#
# def createConsumable(fileName):
#     with open(fileName, 'rb') as file:
#         img_test = file.read()
#         bytes_test = bytearray(img_test)
#
#
#     # process using image bytes
#     response = client.analyze_document(Document={'Bytes': bytes_test}, FeatureTypes=['FORMS'])
#
#     # Get the text blocks
#     blocks=response['Blocks']
#
#     processBlocks(blocks, fileName)
#
# def processBlocks(blocks, fileName):
#
#     file_name_extracted = fileName.split("/")[-1]
#
#     doc_json = []
#     for count, block in enumerate(blocks):
#         if block["BlockType"] == "WORD" or block["BlockType"] == "LINE":
#             inside_json = {}
#             inside_json["index"] = count;
#             inside_json["value"] = block["Text"];
#             inside_json["confidence"] = block["Confidence"];
#             inside_json["type"] = block["BlockType"];
#             doc_json.append(inside_json);
#
#     jsonFileName = file_name_extracted.split(".")[0]+".json"
#
#     with open(jsonFileName, 'w') as fp:
#         json.dump(doc_json, fp, indent=4)


def cloudVision(fileLoc, file_name_extracted):
    googleVision = {}

    with open(fileLoc, 'rb') as image_uri:
        image_content = image_uri.read()
        # content = base64.b64encode(image_content)
    image = types.Image(content=image_content)
    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    resp = {
        "paragraphs": [],
        "words": []
    }

    for page in document.pages:
        pg_index = 0
        for block in page.blocks:
            for para_index, paragraph in enumerate(block.paragraphs):
                pg_index += 1
                para_text = ""
                for word_index, word in enumerate(paragraph.words):
                    word_text = ""
                    for symbol in word.symbols:
                        word_text += symbol.text
                    word_data = {"value": word_text, "confidence": word.confidence, "type": "word",
                                 "word_index": word_index + 1, "para_index": pg_index}
                    resp["words"].append(word_data)
                    para_text += word_text + " "

                para_data = {"value": para_text.strip(), "confidence": paragraph.confidence, "type": "paragraph",
                             "para_index": pg_index}
                resp["paragraphs"].append(para_data)

    googleVision["engine"] = "googleCloudVision"
    googleVision["result"] = resp

    jsonFileName = file_name_extracted.split(".")[0] + ".json"


    with open(jsonFileName, 'w') as fp:
        json.dump(resp, fp, indent=4)


extract_details(dir_name)

