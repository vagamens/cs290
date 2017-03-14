from random import randint
import time

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
	"""docstring for Lines"""
	lines = {}

	lines['acti']['sceneI'] = [{'image': 'boat.png', 'people':['viola', 'captain', 'sailors']},
					 {'name':'Viola', 'line': 'What country, friends, is this?'},
					 {'name':'Captain', 'line': 'This is Illyria, lady.'},
					 {'name':'Viola', 'line': """And what should I do in Illyria?
				 								 My brother he is in Elysium.
			 									 Perchance he is not drown'd: what think you, sailors?"""
			 	 	 },
					 {'name':'Captain', 'line': 'It is perchance that you yourself were saved.'},
					 {'name':'Viola', 'line': 'O my poor brother! and so perchance may he be.'},
					 {'name':'Captain', 'line': """True, madam: and, to comfort you with chance,
				 								   Assure yourself, after our ship did split,
			 									   When you and those poor number saved with you
			 									   Hung on our driving boat, I saw your brother,
			 									   Most provident in peril, bind himself,
			 									   Courage and hope both teaching him the practice,
			 									   To a string mast that lived upon the sea;
			 									   Where, like Arion on the dolphin's back,
			 									   I saw him hold acquaintance with the waved
			 									   So long as I could see."""},
					  {'name':'Viola', 'line': """For saying so, there's gold:
					  							  Mine own escape unfoldeth to my hope,
					  							  Where to thy speech serves for authority,
					  							  The like of him. Know'st though this counrty?
					  						   """},
					  {'name':'Captain', 'line': """Ay, madam, well: for I was bred and born
					  								Not three hours' travel from this very place.
					  						     """},
					  {'name':'Viola', 'line': 'Who governs here?'},
					  {'name':'Captain', 'line': 'A noble duke, in nature as in name.'},
					  {'name':'Viola', 'line': 'What is the name?'},
					  {'name':'Captain', 'line': 'Orsino.'},
					  {'name':'Viola', 'line': """Orsino! I have heard my father name him:
					  							  He was a bachelor then.
					  						   """},
					  {'name':'Captain', 'line': """And so is now, or was so very late:
					  								For but a month ago I went from hence,
					  								And then \'twas freshin murmur, -- as, you know,
					  								What gread ones do the less will prattle of, --
					  								THat he did seek the love of fair Olivia.
					  							 """},
					  {'name':'Viola', 'line': ''},
					  {'name':'Captain', 'line': ''},
					  {'name':'Viola', 'line': ''},
					  {'name':'Captain', 'line': ''}
					  {'name':'Viola', 'line': ''},
					  {'name':'Captain', 'line': ''},
					  {'name':'Viola', 'line': ''},
					  {'name':'Captain', 'line': ''},
					  {'name':'Viola', 'line': ''},
					  {'name':'Captain', 'line': ''}
					  {'name':'Viola', 'line': ''},
					  {'name':'Captain', 'line': ''},
					  {'name':'Viola', 'line': ''},
					  {'name':'Captain', 'line': ''},
					  {'name':'Viola', 'line': ''},
					  {'name':'Captain', 'line': ''}			 		
					]

	lines['actii'] = [{'name':'', 'line': ''},
					  {'name':'', 'line': ''},
					  {'name':'', 'line': ''},
					  {'name':'', 'line': ''},
					  {'name':'', 'line': ''},
					  {'name':'', 'line': ''}
					 ]

	lines['actiii'] = [{'name':'', 'line': ''},
					   {'name':'', 'line': ''},
					   {'name':'', 'line': ''},
					   {'name':'', 'line': ''},
					   {'name':'', 'line': ''},
					   {'name':'', 'line': ''}
					  ]
					  
	lines['activ'] = [{'name':'', 'line': ''},
					  {'name':'', 'line': ''},
					  {'name':'', 'line': ''},
					  {'name':'', 'line': ''},
					  {'name':'', 'line': ''},
					  {'name':'', 'line': ''}
					 ]

	@staticmethod
	def nextScene(act, scene):
		pass
		