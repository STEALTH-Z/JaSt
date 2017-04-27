#!/usr/bin/python
 
'''
	Configuration file storing the mapping between every esprima token and their corresponding integer. 
	Complete list: <https://github.com/jquery/esprima/blob/master/src/token.ts>.
'''


tokensDico = { 
	'Boolean' : 0,
	'<end>' : 1,
	'Identifier' : 2,
	'Keyword' : 3,
	'Null' : 4,
	'Numeric' : 5,
	'Punctuator' : 6,
	'String': 7,
	'RegularExpression' : 8,
	'Template' : 9,
	'LineComment' : 10,
	'BlockComment' : 11

}
