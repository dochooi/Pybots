import sys


def sorry():
    print("sorry i dont understand")
def badword():
        sys.exit()
def exit():
    sys.exit()

def meme():
    print("21")
def creator():
 print("Doc hooi did and i was made on python")
 print("check doc out at this link!: https://www.youtube.com/channel/UC2oKxyVyqEta9a3f3Wb8zHQ")
while True:



    userInput = input(">>> ")
    if userInput in['hi','HI','Hi','Hello','hello','HELLO','']:
        print("Hello")

    elif userInput in ['will you marry me','can we get married','can i be your wife/husband']:
      print("No")
    elif userInput in ['fuck','fuck you','shit','bitch','dumbass','asshole']:
        badword()
    elif userInput in ['exit','EXIT','Exit','Bye','bye','BYE']:
        print("Bye!")
        exit()
    elif userInput in ['9+10','9 + 10','Whats 9+10','Whats 9 + 10','whats 9 + 10','whats 9+10']:
        meme()
    elif userInput in ['who made you','Who made you?','Who made you','who made you?']:
        creator()


    else:
      sorry()
