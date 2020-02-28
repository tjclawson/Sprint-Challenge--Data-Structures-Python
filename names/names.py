import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
tree = BinarySearchTree("middle")
for name_1 in names_1:
    tree.insert(name_1)
for name_2 in names_2:
    if tree.contains(name_2):
        duplicates.append(name_2)

# original runtime was O(n^2) (technically O(x * y), assuming x and y have similar length it is approximately O(n^2))
# because for each name in name_1, it looped all the way through name_2. The new solution has a run time that
# technically is also O(n^2) as well because the worst case for a binary tree search is O(n), but that is assuming that
# the tree is fully unbalanced. But initializing the tree with "middle" as the root (m is the middle name of the
# alphabet) and assuming starting letters of names are evenly distrubted, our tree should be roughly balanced or
# complete, giving a search time of log n. Therefore since we loop through name_1 to add all names to the tree, runtime
# of n, and then search the approximately balanced tree, log n, our final runtime is O(n log n)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

duplicates = set(names_1) & set(names_2)
