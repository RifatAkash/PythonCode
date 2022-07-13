#myset = set(["a", "b", "c"])
#print(myset)
#myset.add("d")
#print(myset)
#frozenset
#normal_set = set(["d" , "e", "f"])
#print(normal_set)
#frozen_set =frozenset(["p", "q", "r"])
#print(frozen_set)

#adding elements

#people = {"akash", "rifat", "mahmud"}
#print(people)
##   people.add(i)
#print(people)

#union operation

#people = {"jack", "alex", "tom"}
#guy = {"cat", "dog", "mice"}
#passion = {"cricketer", "soccer", "badminton"}
##population = people.union(guy)
##population = people|passion
#print(population)

##intersection
set1 = set()
set2 = set()
for i in range(5) :
    set1.add(i)
for i in range(3,9) :
    set2.add(i)
set3 = set1|set2
#set3 = set1.intersection(set2)
set4 = set1 & set2
if set3>set4:
    print("s3 supriest")
elif set3<set4:
    print("s3 is a subset of s4")
else:
    print("they are same")

set5 = set3 - set4
print(set5)
set5.clear()
print(set5)