scores=[56.7, 102.3, 88.9, 45.2, 120.8]

round_scores=[]

for i in scores:
    round_scores.append(round(i))

print("Original list:",scores)
print("Rounded list:",round_scores)
