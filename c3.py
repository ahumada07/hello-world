with open('/Users/saahumad/Documents/MyPythonScripts/pythonchallenge.com/c3.html') as file:
	ws_text = file.read()
text=ws_text.replace('\n',"")
count = 0
new_text = ''
tmp = ''
sw = False
for i in range(0,len(text)):
	if text[i].islower():
		if text[i-3:i].isupper() and text[i+1:i+4].isupper():
			if text[i-4].islower() and text[i+4].islower():
				new_text+=text[i]
print(new_text)

