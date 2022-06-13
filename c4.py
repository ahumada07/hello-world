from urllib.request import urlopen

nothing = 12345
while True:
	with urlopen(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}') as response:
		body = str(response.read())
		try:
			nothing = int(body.split()[-1].replace("'",""))			
			if nothing == 16044:
				nothing = nothing/2
		except:
			print(body)
			break


#result:b'peak.html'
#[Finished in 117.1s]