## Returns all frequent 2-itemsets
def level2_candidate_gen(L, phi, MIS, support_count):
	i = 0
	temp_list = []
	for l in L:
		i +=1
		if support_count[l] >= MIS[l]:
			for h in L[i:]:
				if support_count[h] >= MIS[l] and abs(support_count[h] - support_count[l]) <= phi:
					tupple_to_be_added = l,h
					temp_list.append(tupple_to_be_added)
	return temp_list

# Candidate Generation - Joining and Pruning of itemsets
def MSCandidate_gen(F, phi, support_count, k, MIS):
	temp_list = []
	i=0
	for f1 in F:
		for f2 in F:
			if f1 != f2:
				if (f1[len(f1)-1]<f2[len(f2)-1]) and (f1[:-1] == f2[:-1]) and abs(support_count[f1[len(f1)-1]] - support_count[f2[len(f2)-1]]) <= phi:
					temp_list.append(f1+f2[-1:])
					c = f1+f2[-1:]

					for k in range(1,len(c)+1):
						s = c[:k-1] + c[k:]
						if c[0] in s or MIS[c[1]] == MIS[c[0]]:
							if s not in F:
								temp_list.remove(c)
								break

	return temp_list


