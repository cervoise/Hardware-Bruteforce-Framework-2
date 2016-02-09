import argparse

from Classes import Analyzer

parser = argparse.ArgumentParser(description='Analyze screenshots from an attack with control samples')
parser.add_argument('-s','--screenshots', help='Directory with the screenshots', required=True)
parser.add_argument('-c','--controlSamples', help='Directory with the control samples screen', required=True)
parser.add_argument('-p','--passwordsFile', help='Passwords file used for the attack', required=True)
parser.add_argument('-o','--output', help='Output file (default analyze.csv)', default='analyze.csv', required=False)
args = vars(parser.parse_args())

result = Analyzer.Analyzer(args['controlSamples'], args['screenshots'], args['passwordsFile'])
result.writeCsv(args['output'])