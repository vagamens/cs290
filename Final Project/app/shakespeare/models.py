import re
import time
from flask import url_for
from random import randint

class Insult(object):

	words = [[], [], []]

	words[0] = ["artless", "bawdy", "beslubbering", "bootless", "churlish",
				"cockered", "clouted", "craven", "currish", "dankish",
				"dissembling", "droning", "errant", "fawning", "fobbing",
				"froward", "frothy", "gleeking", "goatish", "gorbellied",
				"impertinent", "infectious", "jarring", "loggerheaded",
				"lumpish", "mammering", "mangled", "mewling", "paunchy",
				"pribbling", "puking", "puny", "qualling", "rank", "reeky",
				"roguish", "ruttish", "saucy", "spleeny", "spongy", "surly",
				"tottering", "unmuzzled", "vain", "venomed", "villainous",
				"warped", "wayward", "weedy", "yeasty", "cullionly", "fusty",
				"caluminous", "wimpled", "burly-boned", "misbegotten", "odiferous",
				"poisonous", "fishified", "Wart-necked"
				]

	words[1] = ["base-court", "bat-fowling", "beef-witted", "beetle-headed",
				"boil-brained", "clapper-clawed", "clay-brained",
				"common-kissing", "crook-pated", "dismal-dreaming",
				"dizzy-eyed", "doghearted", "dread-bolted", "earth-vexing",
				"elf-skinned", "fat-kidneyed", "fen-sucked", "flap-mouthed",
				"fly-bitten", "folly-fallen", "fool-born", "full-gorged",
				"guts-griping", "half-faced", "hasty-witted", "hedge-born",
				"hell-hated", "idle-headed", "ill-breeding", "ill-nurtured",
				"knotty-pated", "milk-livered", "motley-minded", "onion-eyed",
				"plume-plucked", "pottle-deep", "pox-marked", "reeling-ripe",
				"rough-hewn", "rude-growing", "rump-fed", "shard-borne",
				"sheep-biting", "spur-galled", "swag-bellied", "tardy-gaited",
				"tickle-brained", "toad-spotted", "unchin-snouted", "weather-bitten", 
				"whoreson", "malmsey-nosed", "rampallian", "lily-livered", "scurvy-valiant",
				"brazen-faced", "unwash'd", "bunch-back'd", "leaden-footed", "muddy-mettled",
				"pigeon-liver'd", "scale-sided"
				]

	words[2] =  ["apple-john", "baggage", "barnacle", "bladder", "boar-pig",
				"bugbear", "bum-bailey", "canker-blossom", "clack-dish",
				"clotpole", "coxcomb", "codpiece", "death-token", "dewberry",
				"flap-dragon", "flax-wench", "flirt-gill", "foot-licker",
				"fustilarian", "giglet", "gudgeon", "haggard", "harpy",
				"hedge-pig", "horn-beast", "hugger-mugger", "joithead",
				"lewdster", "lout", "maggot-pie", "malt-worm", "mammet",
				"measle", "minnow", "miscreant", "moldwarp", "mumble-news",
				"nut-hook", "pigeon-egg", "pignut", "puttock", "pumpion",
				"ratsbane", "scut", "skainsmate", "strumpet", "varlot",
				"vassal", "whey-face", "wagtail", "knave", "blind-worm", "popinjay",
				"scullian", "jolt-head", "malcontent", "devil-monk", "toad", "rascal",
				"Basket-Cockle"
				]

	@staticmethod
	def generateInsult():
		s = ""
		s = s + Insult.words[0][randint(0, len(Insult.words[0])-1)]+" "
		s = s + Insult.words[1][randint(0, len(Insult.words[1])-1)]+" "
		s = s + Insult.words[2][randint(0, len(Insult.words[2])-1)]
		return s

class Lines(object):
	"""parse and collecte script lines"""
	@staticmethod
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
		return Lines.removeWhiteSpace(line)

	@staticmethod
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

	@staticmethod
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


	@staticmethod
	def getLines():
		lines = {1:{1:[], 2:[], 3:[], 4:[]}, 2:{}, 3:{}, 4:{}}
		
		with open("app/shakespeare/static/script.md", 'r') as f:
			act = 0
			scene = 0
			l = {'name':'', 'line':''}
			for line in f:
				name, line = Lines.getName(line)
				line = line
				if name != None:
					lines[act][scene].append(l)
					l = {}
					l['name'] = name
					l['line'] = ''
				if line[0] == "#":
					num = Lines.parseRoman(line)
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
					l['line'] = l['line']+Lines.removeWhiteSpace(line)+"\n"

		for act in lines:
			for scene in lines[act]:
				for line in range(len(lines[act][scene])):
					lines[act][scene][line]['line'] = Lines.removeWhiteSpace(lines[act][scene][line]['line'])
				for line in range(len(lines[act][scene]), 0):
					if lines[act][scene][line]['line'] == '':
						if lines[act][scene][line]['name'] == '':
							lines[act][scene].pop(line)
		return lines

	@staticmethod
	def getScene(act, scene):
		lines = Lines.getLines()
		print lines[act][scene]
		return lines[act][scene]

	@staticmethod
	def getNextScene(act, scene):
		lines = Lines.getLines()
		if scene == len(lines[act])-1:
			return (act+1, 1, Lines.getScene(act+1, 1))
		else:
			return (act, scene+1, Lines.getScene(act, scene+1))