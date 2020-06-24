#This code is optional for generating List with help of Random
def Generat_Unordard_List(From, To, Length):
    import random
    List = random.sample(range(From, To),Length)
    return List



def Find_Max_Sum_in_sequence(List):
    Sum_Till_Now = 0
    Max_Till_Now = 0
    for i in range(0, len(List),1):
        Sum_Till_Now = Sum_Till_Now + List[i]
        if Sum_Till_Now < 0:
            Sum_Till_Now = 0
        if Sum_Till_Now > Max_Till_Now:
            Max_Till_Now = Sum_Till_Now
    return Max_Till_Now
x = Generat_Unordard_List(-10, 10, 8)
print(x)
max = Find_Max_Sum_in_sequence(x)
print(max)
