submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

set1 = set(submitted)
set2 = set(attended)
attended_and_submitted = set1.intersection(set2)
print(attended_and_submitted)

print(submitted is attended)

attended = [x for x in submitted if x in attended]
print(attended)