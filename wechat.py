import itchat

def login():
    itchat.auto_login()


def sendInfo(remarkname, msg):
    try:
        author = itchat.search_friends(remarkName=remarkname)[0]
        # print(author)
        author.send(msg)
    except:
        print(remarkname + ' warning!')