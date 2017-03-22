import re

def removeWhiteSpace(line):
	if(line == '' or line == '\n'):
		return ''
	if(line[0] == "\t"):
		line = line[1:]
	elif(line[0] == ' '):
		line = line[1:]
	elif(line[-1] == ' '):
		line = line[:-1]
	elif(line[-1] == '\n'):
		line = line[:-1]
	else:
		return line
	return removeWhiteSpace(line)

def getName(line):
	if re.match("^[*]", line[0]):
		index = 2
		for i in range(2, len(line)):
			if re.match("[*]", line[i]):
				index = i
				break
		name = line[2:index]
		line = line[index+3:]
	else:
		return (None, line)
	return (name, line)

def parseRoman(line):
	line = line.split(' ')[2]
	val = 0
	for i in range(len(line)):
		if line[i] == 'I':
			val+=1
		elif line[i] == 'V':
			if val > 0:
				val = 5-val
			else:
				val+=5
	return val


def getLines():
	lines = {1:{1:[], 2:[], 3:[], 4:[]}, 2:{}, 3:{}, 4:{}}
	
	with open("static/script.md", 'r') as f:
		act = 0
		scene = 0
		l = {'name':'', 'line':''}
		for line in f:
			name, line = getName(line)
			line = line
			if name != None:
				lines[act][scene].append(l)
				l = {}
				l['name'] = name
				l['line'] = ''
			if line[0] == "#":
				num = parseRoman(line)
				if line[1] == ' ':
					act = num
					lines[act] = {}
				elif line[1] == "#":
					scene = num
					lines[act][scene] = []
			if line[0] == "#":
				pass
			elif line[0] == '[':
				pass
			else:
				l['line'] = l['line']+removeWhiteSpace(line)+"\n"

	for act in lines:
		for scene in lines[act]:
			for line in range(len(lines[act][scene])):
				lines[act][scene][line]['line'] = removeWhiteSpace(lines[act][scene][line]['line'])
	return lines

lines = getLines()

print lines