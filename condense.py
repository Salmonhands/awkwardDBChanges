#!/usr/local/bin/python3

# Script to merge unique records based on a specific constant field
#
# Uses: 	When you have a lovely, well-designed database that you export data from
#			but have to import it into some heathen's system that wants data that they
#			obviously never work with because this is a useless format.

# Usage:	condense.py -i <inputfile> -o <outputfile>
#				Condense <inputfile> into <outputfile>
#			condense.py -h
#				Display syntax

# Input example
# id_user, date_access
# 0000001, 01/01/2010
# 0000001, 01/02/2010
# 0000001, 01/03/2010
# 0000002, 03/01/2011

# Output example
# id_user, date_access
# 0000001, 01/01/2010, 01/02/2010, 01/03/2010
# 0000002, 03/01/2011

import sys, getopt	#argument parsing
import csv 			#managing csv

# Settings
KCompareCol = 0
KCombineCol = 1
KCombineSymbol = "|"
KCommandSyntax = "test.py -i <inputfile> -o <outputfile>"

# Performs the guts of the operation
def condense(infile,outfile):
	with open(infile, newline='') as rf:
		with open(outfile, 'w', newline='') as wf:
			reader = csv.reader(rf)
			writer = csv.writer(wf)

			prev_line = next(reader)
			for row in reader:
				if prev_line[KCompareCol] != row[KCompareCol]:
					writer.writerow(prev_line)
				else:
					row[KCombineCol] = prev_line[KCombineCol] + KCombineSymbol + row[KCombineCol]
				prev_line = row

# Input processing / validation
def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:", ["ifile=","ofile="])
	except getopt.GetoptError:
		print("----------Syntax Error--------------")
		print(KCommandSyntax)
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print(KCommandSyntax)
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	#print('Input file is: ', inputfile)
	#print('Output file is: ', outputfile)
	condense(inputfile,outputfile)

if __name__ == "__main__":
	main(sys.argv[1:])

