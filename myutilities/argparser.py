import argparse

# instantiates the argparser and creates the --h or --help command
parser = argparse.ArgumentParser(description='Nicle little CL app')

# adding positional arguments
parser.add_argument('name', help='Just your name, nothing special')

# adding optional argument
parser.add_argument('-p', '--profession', help='your noble profession')

# adding flags 
parser.add_argument('-c','--cool', action='store_true', help='Add a little cool')

#creating argument parser
args = parser.parse_args()


#leveraging arguments that are parsed in code
print("Your name is what? " + args.name)

if args.cool:
	cool_addition = ' and draggon tamer'
else:
	cool_addition = ''

if args.profession:
	print("What is your profession? a " + args.profession + cool_addition)