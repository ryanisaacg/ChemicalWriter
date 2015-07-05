import json
import sys
elemText = ""
with open("elements.json", "r") as file:
	elemText = file.read()
elemText = elemText
elements = json.loads(elemText.upper())

def chemwrite(string, chemical = "", position = 0):
	global elements
	if position >= len(string):
		return chemical
	if string[position] in elements:
		result = chemwrite(string, chemical + string[position], position + 1)
		if result: return result
	if position < len(string) - 1:
		if string[position:position + 2:] in elements:
			return chemwrite(string, chemical + string[position] + string[position + 1].lower(), position + 2)

def getElements(string):
	i = 0
	elementList = []
	while i < len(string):
		if i + 1 < len(string) and string[i + 1] != string[i + 1].upper():
			elementList.append(str(elements[string[i:i + 2:].upper()]))
			i += 2
		else:
			elementList.append(str(elements[string[i]]))
			i += 1
	return elementList

def main():
	string = sys.argv[1] if len(sys.argv) > 1 else input("Enter a string to write: ")
	string = string.upper().replace("\n", "").replace("\t", "").replace(" ", "").replace("\r", "")
	chemstring = chemwrite(string)
	elementList = getElements(chemstring)
	print(chemstring)
	print(elementList)
main()
