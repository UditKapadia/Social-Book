def creatpost():
    global post
    post=open("creatpost.txt","a")
    user_post=open(username+".txt","a")
    
    post.write(
                "\n\n"
                + "Timestamp: {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
            )
    
    post.write("\n\n\n" + "Posted by:" + username)
    print("\n\n\n"+"You can write your content below")
    pst=input()
    post.write( "\n"
        + "*****************************\n"
        +pst+ "\n"+   
        "\n*****************************")
    post.close
    user_post.write("\n\n"
                + "Timestamp: {:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
    user_post.write("\n"
        + "*****************************\n"
        +pst+ "\n"+   
        "\n*****************************")
    user_post.close
    press=input("Press spacebar to continue or press 0 to exit")
    if(press==" "):
        print("mansi sanskutri")
    else:
        exit()
def feed():
    post=open("creatpost.txt","r")
    buf=post.read()
    print(buf)
    post.close


