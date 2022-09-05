#imoprt necessary libraries
import sys
import re
import pickle
#declaring dict and idList here for simplicity
myDict = {}
idList = []
#main method
def main():
	#check if system arguments for file name exist
	if len(sys.argv) > 1:
		arg_input = sys.argv[1]
		yy = process(arg_input)#get file name and call process funtion to split it up
		if yy == 1:#if duplicate ids are found, the process metho aborts and returns 1
			print("Error: Duplicate IDs, abort")
			return(0)
#throw error if file name not provided
	else:
		Print("Error: Did not specify file path as System Argument")
		return(0)
#pickling and unpickling the dictionary
	pickle.dump(myDict, open('dict.p', 'wb'))
	dict_in = pickle.load(open('dict.p', 'rb'))
#iterating through the list of dictionary keys and calling the display function from the person class	
	for x in dict_in.keys():
		dict_in[x].display()
#process method responsible for taking file name, splitting lines based on commas, correcting errors, and builing dict
def process(x):	
	f = open(x, 'r')#open up file given file name 'x' as 'f'
	toggle = False#simple boolean toggle to ignore first line
	for line in f:
		if toggle:#true for every line besides first
			splits = line.split(",")#splits is an array created by splitting the line
			p = person(splits[0],splits[1],splits[2],splits[3],splits[4])#each element of splits is an argument of persons init
			if len(idList) != len(set(idList)):#checking if there are no duplicate ids
				return(1)
			myDict[splits[3]] = p#splits[3] is id, so the keys of the dict is the id
		else:
			toggle = True
	f.close()
	return(0)

class person:#class for the person object
	def __init__(self,last,first,mi,ids,phone):
		self.last = last.capitalize()#capitalize first and last name
		self.first = first.capitalize()
		if mi == "":#if middle initial is emply set to X, and capitalize regardless
			mi = "X"
		self.mi = mi.capitalize()
		regs = re.search("^[A-Z]{2}[0-9]{4}$", ids)#regex for id, while id doesnt match, keep prompting user
		while not regs:
			print("ID invalid: " + ids)
			ids = input("ID is two letters followed by 4 digits\nPlease enter a valid id: ")
			regs = re.search("^[A-Z]{2}[0-9]{4}$", ids)
		self.ids = ids
		idList.append(ids)#add id to idlist	
		phone = phone[:-1]#remove newline character from phone number
		regs2 = re.search("^[0-9]{3}-[0-9]{3}-[0-9]{4}$", phone)#regex for phone, while phone doesnt match, keep prompting user
		while not regs2:
			print("Phone " + phone + " is invalid: ")
			phone = input("Enter phone number in form 123-456-7890\nEnter phone number: ")
			regs2 = re.search("^[0-9]{3}-[0-9]{3}-[0-9]{4}$", phone)
		self.phone = phone
	def display(self):#display method which properly formats and outputs all variables of the person class
		print("Employee id: "+ self.ids + "\n       " + self.first+" " +self.mi + " "+ self.last + "\n       " +self.phone)

main()#call main to kick things off