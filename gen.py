import random
from collections import OrderedDict

buys = OrderedDict()
buys['pete'] = 10
buys['anand'] = 20
buys['ro'] = 5
buys['laurenh'] = 20
buys['adam'] = 10
buys['derek'] = 20
buys['beth'] = 3
buys['eddie'] = 10
buys['stacy'] = 10
buys['bulboff'] = 10
buys['will'] = 20

total = reduce(lambda x,y: x+y, buys.values())
slots = total * 2
hours = 31 * 24
blocksize = round(float(hours)/slots)

print 'tickets bought', total
print 'total slots', slots
print 'hours in december', hours
print 'block size in hours', blocksize

tickets = {}

def generateUniqueBlock():
	while True:
		dd = random.randint(2, 31)
		hh = random.randint(0, (24/blocksize)-1)
		
		for t in reduce(lambda x,y: x+y, tickets.values()):
			if t[0] == dd and t[1] == hh:
				return generateUniqueBlock()
		
		return (dd, hh)

for buyer in buys:
	print buyer
	tickets[buyer] = []
	for n in range(buys[buyer]):
		tup = generateUniqueBlock()
		tickets[buyer].append(tup)
	
	tickets[buyer].sort()
	for t in tickets[buyer]:
		print 'december', t[0], 'from', '%02d:00' % (t[1]*3), 'o''clock to', '%02d:59' % (t[1]*3+2)
	print ''
	
print 'public'
all = reduce(lambda x,y: x+y, tickets.values())
all.sort()
for t in all:
	print 'december', t[0], 'from', '%02d:00' % (t[1]*3), 'o''clock to', '%02d:59' % (t[1]*3+2)