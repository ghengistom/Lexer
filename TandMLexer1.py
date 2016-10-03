#!/usr/bin/env python
import sys
#we are importing sys so we can run our program with arguements

class Token():
    def __init__(self, token, lexeme):
        self.lexeme = lexeme
        self.token = token
        
    def __str__(self):
        return "<token:{},                lexeme:   '{}'>".format(self.token, self.lexeme)

#need to add all the keywords these are some
class tmlexer():
    def __init__(self):
        self.keywords = ['while','read','return','if','endif','else','integer','boolean','real']
        self.separators = ['(',')',';','{','}',',','$$','[',']',':']
        self.operators = ['<','*','+','-',':=','/','>','=']
        self.source_file = None

# implement a way to get a text file in here
# retrieve_tokens() this will iterate through the strings of text
    def retrieve_tokens(self):
        with open(self.source_file, 'r+') as source:
            for line in source:
                string = self.add_white(line)
                for token in string.split():
                    yield self.is_it_token(token)

# adds whitespace required to separate otherwise adjaced identifiers, keywords, reals, and ints
    def add_white(self, string):
        single_ops = ['+','-','*','/','!','=','>','<']
        for op in single_ops + self.separators:
#	    fill in with whitespace
            string = string.replace(op, " {} ".format(op))
        string = string.replace(" =  = ", " == ")
        string = string.replace(" !  + ", " != ")
        return string

# classifies things into categories of operators, seps, keywords, ints, reals, ident, unknown
    def is_it_token(self, string):
        if string in self.operators:
            token = Token('Operator', string)
        elif string in self.separators:
            token = Token('Separator', string)
        elif string in self.keywords:
            token = Token('Keyword', string)
        else:
            token = self.token_machine(string)
        return token

# if it's not a operator, separator, keyword, then it is either a: int,real, ident, or unknown
    def token_machine(self, string):
        if self.int_fsm(string):
            token = Token('Int', string)
        elif self.fsm_for_reals(string):
            token = Token('Real', string)
        elif self.ident_fsm(string):
            token = Token('Identifier', string)
        else:
            token = Token('Unknown', string)
        return token

# 		3 finite state machines implemented to determine int, reals, and idents


# this is the finite state machine to determine if something is a real numbers
# the accepted state is state 2, the burn state is state 3
    def fsm_for_reals(self, string):
	#pre: valid string given as the argument
	#post: will return true if accepted, else False
        table = [[0,1,3],[2,3,3],[2,3,3],[3,3,3]]
        accepted_state = 2
        state = 0
        for i in range(len(string)):
            if string[i].isdigit():
                inputs=0
            elif string[i] == '.':
                input=1
            else:
                input=2
            state = table[state][input]
        if state == accepted_state:
            accepted = True
        else:
            accepted = False
        return accepted

# this is the finite state machine to determine if something is an identifier
# state 2 is the accepted state, state 3 is the burn state
    def ident_fsm(self, string):
        table = [[1,3,3,3],[2,2,2,3],[2,2,3,3],[3,3,3,3]]
        accepted_state = 2
        state = 0
        for i in range(len(string)):
            if string[i].isalpha():
                input=0
            elif string[i].isdigit():
                input=1
            elif string[i] == '_':
                input=2
            else:
                input=3
            state = table[state][input]
        if state == accepted_state:
            accepted = True
        else:
            accepted = False
        return accepted

# this is the finite state machine to determine if something is an integer
# state 0 is the accepted state, state 1 is the burn state
    def int_fsm(self, string):
        table = [[0,1],[1,1]]
        accepted_state = 0
        state = 0
        for i in range(len(string)):
            if string[i].isdigit():
                input=0
            else:
                input=1
            state = table[state][input]
        if state == accepted_state:
            accepted = True
        else:
            accepted = False
        return accepted

    def setfile(self, filename):
        self.source_file = filename

# count the tokens 
if __name__=='__main__':
    lex = tmlexer()
    lex.setfile(sys.argv[1])
    token_count = 0
    for token in lex.retrieve_tokens():
        print(token)
        token_count += 1
    print("{} amount of tokens in file.".format(token_count))






