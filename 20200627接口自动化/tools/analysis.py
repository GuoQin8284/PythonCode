import json
import os
import config


def analysis_data(fileName):

    file = config.path + os.sep + "data" + os.sep + fileName
    with open(file=file, mode="r", encoding="UTF-8") as f:
        data_list = [(x,) for x in json.load(f)]
        return data_list