
def promptInput(inD):
	usData = ""
	while not(usData):
		usData = input(inD)
		if(usData):
			return usData.rstrip().lower()

def getInput():
	data = ""
	nonData = True
	name = ""
	sClass = ""
	date = ""
	amount = 0
	descr = ""
	bal = 0
	hasName = False
	hasClass = False
	hasDate = False
	hasAmount = False
	stop = False

	while (nonData):
		name = promptInput("name: ")
		sClass = promptInput("class: ")
		date = promptInput("date: ")
		amount = promptInput("amount: ")
		descr = promptInput("descr: ")
		bal = promptInput("balance: ")
		nonData = False
	return [name,sClass,date,amount,descr,bal]

def hashData(data):
	key = "e67aa24ecf1951ec"
	data += key
	import hashlib
	h = hashlib.md5()
	h.update(data.encode('utf-8'))
	return h.hexdigest()

def showHash(hash):
	print(hash)

if __name__ == "__main__":
	arrData=getInput()
	data = ""
	for d in arrData:
		data += d

	hash = hashData(data)
	showHash(hash)
