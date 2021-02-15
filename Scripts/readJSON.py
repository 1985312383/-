def readJson(file_name=""):
    import json
    if file_name != '':
        strList = file_name.split(".")
        if strList[len(strList) - 1].lower() == "json":
            with open(file_name, mode='r', encoding="utf-8") as file:
                return json.loads(file.read())
