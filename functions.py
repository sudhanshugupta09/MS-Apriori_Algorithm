## Functions
import re
from operator import itemgetter


## Calculate M -> Sorted list of MIS values
def calculate_M(MIS):
	M = sorted(MIS.items(), key=itemgetter(1)) ## M is the list of the values sorted by MIS Values
	return M

## Create List of Items
def create_list_of_items(I, MIS):
	for key, value in MIS.items():
		I.append(key)

## Inital pass over the items list
def init_pass(M,L,MIS,support_count):
	conf_flag = True
	for (i, mis_val) in M:
		if support_count[i] >= MIS[i] and conf_flag:
			L.append(i)
			min_mis_reqiured = MIS[i]
			conf_flag = False
		elif not conf_flag:
			if support_count[i] >= min_mis_reqiured:
				L.append(i)


def check_cannot_be_together(F, cannot_be_together):
	temp = [[],[],[],[],[]]
	frequent_val = 0

	for f in F:
		if len(f)>0:
			for s in f:
				if frequent_val > 0:
					for c in cannot_be_together:
						if set(c).issubset(s):
							pass
						else:
							temp[frequent_val].append(s)
				else:
					temp[frequent_val].append(s)
			frequent_val+=1
	return temp


def check_must_have(F, must_have):
	final_F = [[],[],[],[],[]]
	frequent_val = 0

	for f in F:
		if len(f)> 0:
			temp = set()
			for s in f:
				for must in must_have:
					if frequent_val > 1:
						if must in s:
							temp.add(s)
							continue		
					else:
						if s in must_have:
							temp.add(s)
			final_F[frequent_val-1].extend(list(temp))
		frequent_val += 1
	return final_F

