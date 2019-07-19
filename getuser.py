import itchat

itchat.auto_login(hotReload=True)

friends = itchat.search_friends(name='Bing')
print(friends[0]['UserName']) 