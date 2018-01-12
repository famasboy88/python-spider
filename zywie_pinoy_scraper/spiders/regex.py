import re
mylist = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo"]
r = re.compile("\\bwildcat\\b")
newlist = filter(r.match, mylist)
if not (list(newlist)):
    print("Nothing")
else:
    print("There is")
