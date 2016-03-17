import argparse

parser = argparse.ArgumentParser(description='Clean wordlist with special critera')
parser.add_argument('passwordsFile', help='Input passwords file')
parser.add_argument('-c','--noCaseSensitive', help='Password are not case sensitive', action='store_true')
parser.add_argument('-m','--min', help='Passwords min size', default=1, required=False)
parser.add_argument('-M','--Max', help='Passwords max size', default=64, required=False)
parser.add_argument('--noNumber', help='Password does not allow numbers', required=False, action='store_true')
#parser.add_argument('-o', '--output', required=False)

args = vars(parser.parse_args())


output = []

for line in open(args['passwordsFile']).readlines():
	line = line.rstrip()
	#print len(line) >= int(args['min'])
	if len(line) >= int(args['min']) and len(line) <= int(args['Max']):
		if args['noCaseSensitive']:
			line = line.lower()
		if args['noNumber']:
			for i in range(10):
				line = line.replace(str(i), '') 
		output.append(line)

output = set(list(output))
for elmt in output:
	print elmt
