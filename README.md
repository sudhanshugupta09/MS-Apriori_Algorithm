# MS-Apriori_Algorithm
This is an implementation of MS-Apriori Algorithm to find frequent itemsets during mining over transactional databases.

Apriori is a Data Mining Algorithm for frequent item set using association rules that learns over transactional databases. It proceeds by identifying the frequent individual items in the database and extends them to larger item sets as long as the items appear in the database often. (With certain rules/constraints to define "often"). MS-Apriori is a modified version of Apriori, but instead it uses multiple supports to satisfy the conditions extending them to larger item sets.

Is MS Apriori better? Yes! It accounts for the "rare item support." Apriori only holds 1 minimum support for the entire transaction database. In MS Apriori, we have multiple supports; every item has a min-support. This will improve the effectiveness of the association rules and account for the rare items.


**Sample Transactional Data**
{20, 30, 80, 70, 50, 90}
{20, 10, 80, 70}
{10, 20, 80}
{20, 30, 80}
{20, 80}
{20, 30, 80, 70, 50, 90, 100, 120, 140}

**Sample Parameter File**

*MIS values for all items*
MIS(10) = 0.43
MIS(20) = 0.30
MIS(30) = 0.30
MIS(40) = 0.40
MIS(50) = 0.40
MIS(60) = 0.30
MIS(70) = 0.20
MIS(80) = 0.20
MIS(90) = 0.20
MIS(100) = 0.10
MIS(120) = 0.20
MIS(140) = 0.15

*Other Parameters*
SDC = 0.1
cannot_be_together: {20, 40}, {70, 80}
must-have: 20 or 40 or 50

**Sample Output File**
Frequent 1-itemsets 

    6 : {20}

    Total number of frequent 1-itemsets = 1


Frequent 2-itemsets 

    6 : {80, 20}
Tailcount = 6
    2 : {90, 50}
Tailcount = 2

    Total number of frequent 2-itemsets = 2
