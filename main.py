from datetime import datetime
import json
import time
import requests

url = "https://alchemy-memos.onrender.com/api/memo?openId=2fea7ec8-a339-4c8c-b398-7145f178529e"
tag = "翦商"

def create_memo(t, content):
    t = datetime.strptime(t,"%Y-%m-%d %H:%M") 
    t = int(time.mktime(t.timetuple()))
    content = "#" + tag + "\n" + content
    s = json.dumps({"content": content,
                    "createdTs": t})
    
    print(content, t)
    # r = requests.post(url, data=s)
    # print(r.status_code)


divider = "-------------------"


def read_file():
    f = open("翦商.txt")
    lines = f.readlines()


    index = 0
    while (index + 3) < len(lines):
        t = ""
        content = ""
        page = ""
        if lines[index+3].strip('\n') == divider:
            index += 3
        else:
            index += 4
        t = lines[index-2][:16]
        page_start = lines[index-2].index("页")
        page = lines[index-2][page_start:-1]
        content = lines[index-1]
        create_memo(t, content + page)


    f.close()



if __name__ == "__main__":
    read_file()
