name = input("What is your name? ")

if len(name) == 1:
    print("lazy can't you give me a proper name?")
elif len(name) == 2:
    print("still lazy, i know two letters are better than one but still that's no commitment at all...")
elif len(name) == 3:
    print ("that's a short name " + name + ", but i'll take it")
else:
    print("Welcome to this game i suppose... Jarvis... i meant " + name)
