import marshal

x = {'a': 1, 'b': 2, 'c': {'y': 'string', 'z': ['list','of',4,'items']}}

f = open('test.txt', 'w')
marshal.dump(x, f)
f.close()

f = open('test.txt', 'r')
y = marshal.load(f)

print x
print y
