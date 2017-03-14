import re

def removeWhiteSpace(line):
	if(line == ''):
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

lines = {}

with open("static/playSections/Act I.md", 'r') as f:
	act = 0
	scene = 0
	l = {'name':'', 'line':''}
	for line in f:
		name, line = getName(line)
		line = line
		if line[0] == "#" and line[1] == ' ':
			act = parseRoman(line)
		elif line[0:3] == "###":
			pass
		elif line[0] == "#" and line[1] ==  "#":
			scene = parseRoman(line)
			print "Act: "+str(act)
			print "Scene: "+str(scene)
			lines[act] = {}
			lines[act][scene] = []
		if name != None:
			lines[act][scene].append(l)
			l = {}
			l['name'] = name
			l['line'] = ''
			print name+":"
		if line[0] == "#":
			pass
		elif line[0] == '[':
			print removeWhiteSpace(line)
		else:
			l['line'] = l['line']+removeWhiteSpace(line)+"\n"
			print '  '+removeWhiteSpace(line)

print lines