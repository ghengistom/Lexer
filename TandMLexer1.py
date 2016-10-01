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
	self.separators = ['(',')',';','{','}',',','$$']
	self.operators = ['<','*','+','-',':=']
	self.source_file = None


    def setfile(self, filename):
	self.source_file = filename

# implement a way to get a text file in here
# retrieve_tokens() this will iterate through the strings of text
    def retrieve_tokens(self):
	with open(self.source_file, 'r+') as source:
	    for line in source:
		string = self.add_white(line)
		for token in string.split():
		    yield self.is_it_token(token)

    def add_white(self, string):
        for op in single_ops + self.SEPERATORS:
#	    fill in with whitespace
	        string = string.replace(op, " {} ".format(op))
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
	elif self,fsm_for_reals(string):
	   token = Token('Real', string)
	elif self.identifier_fsm(string):
	   token = Token('Identifier', string)
	else:
	   token = Token('Unknown', string)
	return token


   def fsm_for_reals(self, string):
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


   def ident_fsm(self, string):
	table = [[1,3,3],[1,2,3],[1,2,3],[3,3,3]]
	accepted_state = 1
	state = 0
	for i in range(len(string)):
	    if string[i].isalpha():
		sigma=0
	    elif string[i].isdigit():
	        sigma=1
	    else:
		sigma=2
	    state = table[state][sigma]
	if state == accepted_state:
	    accepted = True
	else:
	    accepted = False
	return accepted

    def int_fsm(self, string):
	table = [[0,1],[1,1]]
	accepted_state = 0
	state = 0
	for i in range(len(string)):
	   if string[i].isdigit():
		sigma=0
	   else:
		sigma=1
	   state = table[state][sigma]
	if state == accepted_state:
	    accepted = True
	else:
	    accepted = False
	return accepted


if __name__=='__main__':
    lex = Lexer()
    lex.set_source_file(sys.argv[1])
    token_count = 0
    for token in lex.get_tokens():
	print(token)
	token_count += 1
    print("{} amount of tokens in file.".format(token_count))






