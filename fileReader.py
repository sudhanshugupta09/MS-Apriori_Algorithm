import re

## Read Transactions from the file
def transaction_read():
	lines = open("data_files/data-2.txt", "r+").readlines()
	final_lines = [line.rstrip('\n') for line in lines]
	transactions = [[int(n) for n in re.split('{|}|, ', line) if n.isdigit()] for line in final_lines]
	return transactions

## Read the parameters and constraints provided
def parameter_read(MIS, must_have, cannot_be_together,phi):
	lines = open("parameter_files/para2-2.txt", "r+").readlines()
	final_lines = [line.rstrip('\n') for line in lines]

	for line in final_lines:

		if line.find("M")> -1:
			key = int(line[line.find("(")+1:line.find(")")])
			value = float((line[line.find("= ")+1:]).strip())
			MIS[key] = value

		if line.find('SDC') > -1:
			phi = float((line[line.find("= ")+1:]).strip())
		
		if line.find('must') > -1:
			must_have = re.findall('[0-9]+',line)

		if line.find('cannot') > -1:
			splits = line.split('{')
			for split in splits:
				s = (list(re.findall('[0-9]+', split)))
				if len(s)>0:
					cannot_be_together.append(list(s))

	cannot_be_together = [tuple(int(x) for x in val) for val in cannot_be_together]
	must_have = [int(val) for val in must_have]
	return MIS, must_have, cannot_be_together,phi

