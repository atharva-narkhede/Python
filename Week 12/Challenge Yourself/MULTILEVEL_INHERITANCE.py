#MULTILEVEL INHERITANCE
#We can implement multi-level inheritance in our application. Let's consider the domain 'Stall' and its types. There exists a multilevel inheritance
#Create a class SilverStall with the following attributes.
#Attributes: name (String), detail (String), owner (Sting), cost (float)
#Total cost computes only the stall cost


class SilverStall:
    def __init__(self, name, detail, owner, cost):
        self.name = name
        self.detail = detail
        self.owner = owner
        self.cost = cost

    def total_cost(self):
        cost_value = self.cost
        print(cost_value)

class GoldStall(SilverStall):
    def __init__(self, name, detail, owner, cost, tv_set):
        super().__init__(name, detail, owner, cost)
        self.tv_set = tv_set

    def total_cost(self):
        cost_value = self.cost + (100 * self.tv_set)
        print(cost_value)

class PlatinumStall(GoldStall):
    def __init__(self, name, detail, owner, cost, tv_set,projector):
        super().__init__(name, detail, owner, cost, tv_set)
        self.projector = projector

    def total_cost(self):
        cost_value = self.cost + (100 * self.tv_set) + (500 * self.projector)
        print(cost_value)


#Main Program
choice = int(input()) # 1 for silver stall, 2 for gold stall and 3 for platinum stall)
stall_name = input()
stall_detail = input()
stall_owner = input()
stall_cost = float(input())

if choice == 1: #SilverStall
    obj = SilverStall(stall_name,stall_detail, stall_owner,stall_cost)
    obj.total_cost()

elif choice == 2: #GoldStall
    tv_set = int(input())
    obj = GoldStall(stall_name,stall_detail, stall_owner,stall_cost,tv_set)
    obj.total_cost()

elif choice == 3: #GoldStall
    tv_set = int(input())
    projector = int(input())
    obj = PlatinumStall(stall_name,stall_detail, stall_owner,stall_cost,tv_set,projector)
    obj.total_cost()

else:
    print('Invalid Choice')
