import yaml

def data(DataFileName,message,test_add_message):

    with open("./data/"+DataFileName,"r",encoding="utf-8") as f:
        data_one=yaml.load(f)
        print(data_one)
        data_two=data_one[message]
        data_three=data_two[test_add_message]
        print(data_three)
        datalist=[]
        for i in data_three.values():
            datalist.append(i)

        print("datalist:",datalist)
        return datalist
