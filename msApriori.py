import functions as fn
import candidateGen 
import fileReader as fr
#import DefaultList


'''
MIS - Minimun Item Support 
must_have - items that should be included in the final list
cannot_be_together - items that cant appear in the same set 
phi - maximum support difference value 
'''
MIS = {}
must_have = []
cannot_be_together = []
phi = 0
F = [[],[],[],[],[],[]]
C = [[],[],[],[],[],[]]
L = []

MIS, must_have, cannot_be_together,phi = fr.parameter_read(MIS, must_have, cannot_be_together,phi)


# Read the transactions from the input_text.txt file
transactions = fr.transaction_read()

# Step 1 - Calculate the value of M
M = fn.calculate_M(MIS)

## initializing the count_values dictionary with zeros for each item
count_values = MIS.copy()
for key,value in count_values.items():
	count_values[(key)] = 0

## updating the counts of the values in the count_values dictionary
for transaction in transactions:
	for item in transaction:
		count_values[item] += 1



support_count = count_values
final_support_count = support_count.copy()
number_of_transactions = len(transactions)
for item, count in support_count.items():
	support_count[item] = float(count/number_of_transactions)

# Step 2 - Initial Pass over M
fn.init_pass(M,L,MIS,support_count)


# Step3: Create Frequent Set 1
for l in L:
	if support_count[l] >= MIS[l]:
		F[1].append(l)
		# print(F)

# Step 4 to 19
tailcount = {}
k = 2

while F[k-1] : ## F[0] being passed as F[1]
	if k == 2:
		C[k].extend(candidateGen.level2_candidate_gen(L, phi, MIS, support_count))

	else:
		C[k].extend(candidateGen.MSCandidate_gen(F[k-1], phi, support_count,k, MIS)) ## C[3], F[2]
	## creating a temporary dictionary
	temp_dict = {} 
	for c in C[k]:
		temp_dict[c] = 0
		tailcount[c] = 0
 
 	## counting the support of all the candidates
	for transaction in transactions:
		for c in C[k]:
			if set(c).issubset(transaction):
				temp_dict[c] += 1
			if set(c[1:]).issubset(transaction):
				tailcount[c] += 1

	for c,value in temp_dict.items():
		if temp_dict[c]/number_of_transactions >= MIS[c[0]]:
			F[k].append(c)
			support_count[c] = temp_dict[c]/number_of_transactions
			final_support_count[c] = temp_dict[c]
	
	k = k + 1 # counter increment

# Must have condidtion
if must_have:
	F = fn.check_must_have(F, must_have)

# Cannot be together condition
if len(cannot_be_together) > 0:
	F = fn.check_cannot_be_together(F, cannot_be_together)

counter = 0
Final_f = []
for val in F:
	if len(val)>0:
		final_dict = dict()
		for s in val:
			final_dict[s] = final_support_count[s]
		Final_f.append(final_dict)

output = ""
f_out = open("result_files/result2-2.txt", "w")

if len(Final_f) is 0:
	output += "Frequent " + "1" + "-itemsets \n\n"
	output += "\n    Total number of frequent " + "1" + "-itemsets = " + "0" + "\n\n\n"

freq_set_num = 1
for frequent_sets in Final_f:
	output += "Frequent " + str(freq_set_num) + "-itemsets \n\n"

	for sets in frequent_sets:
		if freq_set_num == 1:	
			output += "    " + str(Final_f[freq_set_num-1][sets]) + " : " + "{"  + str(sets) + "}\n"
		if freq_set_num > 1:
			output += "    " + str(Final_f[freq_set_num-1][sets]) + " : " + "{" + ", ".join(list(map(str,sets))) + "}\n"
		if freq_set_num > 1:
			output += "Tailcount = " + str(tailcount[sets]) + "\n"

	output += "\n    Total number of frequent " + str(freq_set_num) + "-itemsets = " + str(len(frequent_sets)) + "\n\n\n"
	freq_set_num += 1
f_out.write(output)
f_out.close()
