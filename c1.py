text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

text2 = "map"


alphabet = 'abcdefghijklmnopqrstuvwxyz'

alpha_index = [x for x in enumerate(alphabet)]

alphabet2 = 'cdefghijklmnopqrstuvwxyzab'

for letter in text2:
	if letter in alphabet:
		index = alphabet.index(letter)
		print(alphabet2[index])
	else:
		print(letter)

#using maketrans()

cipher = dict(zip(alphabet,alphabet2))
mapping = text.maketrans(cipher)
new_text = text.translate(mapping)
print(new_text)


