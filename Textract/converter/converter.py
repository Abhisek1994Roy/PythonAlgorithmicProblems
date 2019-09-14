
import json
import sys

# file_name = sys.argv[1]

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass


    return False

def get_values(file_name):
    with open(file_name, 'r') as f:
        response = json.load(f)

    # Get the text blocks
    blocks = response['Blocks']

    getNik(blocks)

    createConsumable(blocks, file_name)

def createConsumable(blocks, file_name):

    file_name_extracted = file_name.split("/")[-1]

    doc_json=[]
    for count,block in enumerate(blocks):
        if block["BlockType"] == "WORD" or block["BlockType"] == "LINE":
            inside_json = {}
            inside_json["index"] = count;
            inside_json["value"] = block["Text"];
            inside_json["confidence"] = block["Confidence"];
            inside_json["type"] = block["BlockType"];
            doc_json.append(inside_json);

    with open(file_name_extracted, 'w') as fp:
        json.dump(doc_json, fp, indent=4)


def getNik(blocks):
    lineArr = []
    wordArr = []

    for block in blocks:
        if block["BlockType"] == "LINE":
            str = block["Text"].lower()
            lineArr.append(str)
            str = str.replace(" ","")
            if is_number(str) and (len(str)==16):
                print(str)
        if block["BlockType"] == "WORD":
            str = block["Text"].lower()
            wordArr.append(str)
            str = str.replace(" ", "")
            if is_number(str) and (len(str)==16):
                print(str)

    try:
        nik_index = lineArr.index("nik")
    except:
        nik_index = -1

    try:
        nama_index = lineArr.index("nama")
    except:
        nama_index = -1

    if nik_index != -1:
        str = (lineArr[nik_index + 1])
        str = str.replace(" ", "")
        if is_number(str) and (len(str) == 16):
            print(str)

    if nama_index != -1:
        str = (lineArr[nik_index + 1])
        str = str.replace(" ", "")
        if is_number(str) and (len(str) == 16):
            print(str)




get_values("/Users/abhisekroy/Abhisek/Python_Algorithmic_Problems/Textract/textract3.json")