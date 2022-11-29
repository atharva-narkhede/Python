#Create a class called py_solution.Write a Python program to get all possible unique subsets from a set of distinct integers.

class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]
n=list(map(int,input().split()))
print(py_solution().sub_sets(n))
