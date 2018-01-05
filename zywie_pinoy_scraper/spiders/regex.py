import re

string = ['spicy chicken', 'butter', 'milk']

list_in = ['we have chicken in here', 'but we don have butter', 'Kyle', 'spicy']
search = "("

for i in string:
    search += ".*" + i + ".*|"

search = search.rstrip("|")
search += ")"

print(search)

r = re.compile(search)
newlist = filter(r.match, list_in)
for i in newlist:
    print(i)
