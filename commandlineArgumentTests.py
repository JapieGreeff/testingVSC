"""
Testing the argument parsing stuff 
"""
import argparse

#default values for arguments that can be passed in from the command line
defaults = {'first':'gold', 'second':'silver', 'third':'bronze'}

# the parser that parses through the arguments that are passed from the command line
parser = argparse.ArgumentParser()
parser.add_argument('first', help = 'please add the colour of the first medal', type = str) 
parser.add_argument('second', help = 'please add the colour of the second medal', type = str) 
parser.add_argument('third', help = 'please add the colour of the third medal', type = str) 
parser.add_argument('-o','--optionalArg', help = 'this is an optional int argument', type = int) 
parser.add_argument('-o2','--optionalArg2', help = 'this is another optional int argument with a default', type = int, default = 0) 
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", help ='do you want the program to be verbose', action="store_true")
group.add_argument("-q", "--quiet", help ='do you want the program to be quiet', action="store_true")  
args = parser.parse_args()
# args is now a namespace with the arguments that were passed
print(args)
print(f'{args.first} {args.second} {args.third}')
if args.optionalArg:
    print('there was an optional arg')