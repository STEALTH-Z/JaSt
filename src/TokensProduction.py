
'''
	Producing tokens from a JavaScript file and converting them into integers.
'''

from slimit.lexer import Lexer

import subprocess # to call Shell commands
import os


def astUsedEsprima(inputFile):
	'''
		Given an input JavaScript file, create a list containing the esprima syntactic elements used.
	'''
	
	'''
		tempFile = 'Tempo.txt';
		subprocess.call("slimit --mangle < " + inputFile + " > " + tempFile, shell = True); # Minify the input file
		
		tFile = open(tempFile,'r');
		s = "var esprima = require('esprima');\nesprima.parse('";
		for line in tFile:
			line = line.replace("'",'"');
			s += line;
		s += "', {}, function (node) {\n\tconsole.log(node.type);\n});"
		#return s;
		
		# TODO: s = "var esprima = require('esprima');\nvar x = javascript_read_from_file(); esprima.parse(x, {}, function (node) {\n\tconsole.log(node.type);\n});"
		
		# var fs = require("fs");
		# var text = fs.readFileSync('/home/aurore/Documents/Code/JS-samples/PbEspAst/0a953c0d44d172394bd1985edf44d52718a2f2a1.bin').toString('utf-8')
		
		tFile.close();
		tFile = open(tempFile,'w');
		
		tFile.write(s);
		tFile.close();
		
		#subprocess.call("node " + tempFile + " > " + outputFile, shell = True); # Produce the list of tokens using esprima
		
		result = subprocess.run(['node' , tempFile ], stdout = subprocess.PIPE).stdout.decode('utf-8');
		os.remove(tempFile);
	'''
	
	result = subprocess.run(['node' , 'JSEsprima/parser.js', inputFile], stdout = subprocess.PIPE).stdout.decode('utf-8');
	# result is a string containing the returned objects of the JS script, separated by '\n'
	syntaxPart = str(result).split('\n'); # Keyword as used in JS
	del(syntaxPart[len(syntaxPart) - 1]); # As last one = ''
		
	return syntaxPart; # The order of the tokens returned resembles a tree traversal using the depth-first algorithm.
	
	
def tokensUsedEsprima(inputFile):
	'''
		Given an input JavaScript file, create a list containing the esprima tokens used.
	'''
	
	'''
		tempFile = 'Tempo.txt';
		subprocess.call("slimit --mangle < " + inputFile + " > " + tempFile, shell = True); # Minify the input file
		
		tFile = open(tempFile,'r');
		s = "var esprima = require('esprima');\nesprima.tokenize('";
		for line in tFile:
			line = line.replace("'",'"');
			s += line;
		s += "', {}, function (node) {\n\tconsole.log(node.type);\n});"
		#return s;
		tFile.close();
		tFile = open(tempFile,'w');
		
		tFile.write(s);
		tFile.close();
		
		#subprocess.call("node " + tempFile + " > " + outputFile, shell = True); # Produce the list of tokens using esprima
		result = subprocess.run(['node' , tempFile ], stdout = subprocess.PIPE).stdout.decode('utf-8');
		os.remove(tempFile);
	'''
	
	result = subprocess.run(['node' , 'JSEsprima/tokenizer.js', inputFile], stdout = subprocess.PIPE).stdout.decode('utf-8');
	# result is a string containing the returned objects of the JS script, separated by '\n'
	tokenPart = str(result).split('\n'); # Keyword as used in JS
	del(tokenPart[len(tokenPart) - 1]); # As last one = ''
		
	return tokenPart;
	
		
	
def tokensUsedSlimit(inputFile):
	'''
		Given an input JavaScript file, create a list containing the SlimIt tokens used.
	'''
	inF = open(inputFile,'r');
	s = '';
	for line in inF:
		s += str(line); # Store the content of the JS file in a string
	inF.close();
	
	#result = subprocess.run(["slimit --mangle < ", inputFile], stdout = subprocess.PIPE).stdout.decode('utf-8');
	
	lexer = Lexer();
	lexer.input(s);

	l = [];

	for token in lexer:
		# Structure of a token: "LexToken(VAR,'var',1,0)"
		tokenPart = str(token).split('(');
		tokenComplete = tokenPart[1].split(','); # Keyword as used in JS
		l += [tokenComplete[0]];
	
	return l;



def tokensToNumbers(tokensDico, tokensList):
	'''
		Convert a list of tokens in their corresponding numbers (as indicated in the tokens dictionary).
	'''

	numbers = [];
	
	for token in tokensList:
		numbers = numbers + [tokensDico[token]];
	
	return numbers;
