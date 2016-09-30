import sys
#we are importing sys so we can run our program with arguements

class token():
    def __init__(self, token, lexeme):
	self.token = token
	self.lexeme = lexeme

    def __str__(self):
	return "<token:{}, lexeme:'{}'>".format(self.token, self.lexeme)

#need to add all the keywords these are some
class tmlexer():
    def __init__(self):
	self.keywords =
['while','read','return','if','endif','else','int']
	self.separators = ['(',')',';']
	self.operators = ['<','*','+','-',':=']
	self.source_file = None



# implement a way to get a text file in here
# retrieve_tokens() this will iterate through the strings of text



# build a function that determines that string is a valid token
	#pre condition: has a valid string given as argument
	#post condition: returns token type for string argument


# int_fsm()
	#pre: valid string given as the argument
	#post: will return true if accepted, else False
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

# real_fsm()
	#pre: Valid string given as arg
	#post: return t if accepted, false otherwise

# identifier_fsm()
	#pre: same as above
	#post: return true if accepted, ....
