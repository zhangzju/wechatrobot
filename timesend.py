import itchat
import threading

itchat.auto_login(hotReload=True)
friends = itchat.search_friends(name='Bing')
username = friends[0]['UserName']

def send_msg():
    itchat.send('老婆大人你最美', toUserName=username)
    timer = threading.Timer(0.1,send_msg)
    timer.start()

if __name__ == "__main__":  
    send_msg() 