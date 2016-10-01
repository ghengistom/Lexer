import sys
#we are importing sys so we can run our program with arguements

class Token():
    def __init__(self, token, lexeme):
	self.token = token
	self.lexeme = lexeme

    def __str__(self):
	return "<token:{}, lexeme:'{}'>".format(self.token, self.lexeme)

#need to add all the keywords these are some
class tmlexer():
    def __init__(self):
	self.keywords = ['while','read','return','if','endif','else','integer','boolean','real']
	self.separators = ['(',')',';']
	self.operators = ['<','*','+','-',':=']
	self.source_file = None


    def setfile(self, filename):
	self.source_file = filename

# implement a way to get a text file in here
# retrieve_tokens() this will iterate through the strings of text
    def retrieve_tokens(self):
	with open(self.source_file, 'r+') as source:
	    for line in source:
		string =self.add_white(line)
		for token in string.split():
		    yield self.isit_token(token)

    def add_white(self, string):
        for op in single_ops + self.SEPERATORS:
	    string = string.replace(" =  = ", " == ")
	    string = string.replace(" !  + ", " != ")
	    return string

    def is_it_token(self, string)
	if string in self.operators:
	    token = Token('Operator', string)
	elif string in self.seperators:
	    token = Token('Separator', string)
	elif string in self.keywords:
	    token = Token('Keyword', string)
	else:
	    token = self.token_fsm(string)
	return token


    def token_machine(self, string):
	if self.int_fsm(string):
	   token = Token('Int', string)
	elif self,fsmforreals(string):
	   token = Token('Real', string)
	elif self.identifier_fsm(string):
	   token = Token('Identifier', string)
	else:
	   token = Token('Unknown', string)
	return token


   def ident_fsm(self, string):
	table = 


    def fsmforreals(self, string):
	#pre: valid string given as the argument
	#post: will return true if accepted, else False
        table = [[1,4,4],[1,2,4],[3,4,4],[3,4,4],[4,4,4]]
        accepted_state = 3
        state = 0
        for i in range(len(string)):
         if string[i].isdigit():
                sigma=0
            else:
                sigma=2
            state = table[state][sigma]
        if state == accepted_state:
            accepted = True
        else:
            accepted = False
        return accepted




# build a function that determines that string is a valid token
	#pre condition: has a valid string given as argument
	#post condition: returns token type for string argument
	if self.int






