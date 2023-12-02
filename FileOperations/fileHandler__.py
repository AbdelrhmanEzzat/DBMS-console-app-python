import json

def read_data():
    try:
        with open('Users.json', 'r') as fileobj:
            print(fileobj)
            data = fileobj.read()
            # print(data)
            dataa = json.loads(data)
            return dataa  # list of dict
    except Exception as e:
        print(e)


def write_data(myinfo):
    try:
        old_data = read_data()  # list of dicts
        with open('Users.json', 'w') as fileobj:
            old_data.append(myinfo)
            # data = json.dumps(["ffff", 'ffff'])
            data = json.dumps(old_data, indent=4)  # convert list of dicts to string
            fileobj.write(data)  # write data to the file ?
    except Exception as e:
        print(e)



