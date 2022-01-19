
population=list()
extreme=int(input("enter the no of peoples for them to get verified about their eligibility to vote:"))
for i in range(1,extreme+1,1):
    population.append(input("enter the age of person:{}".format(i)))
print("here is the list of ages of persons respectively")    
for i in range(0,len(population)):
    print("enter the age of the person: ",i+1,"is :",population[i])
print("USING ENUMERATE")    
for k in enumerate(population):
    print(k)
print("USING * TO PRINT ALL VALUES IN GIVEN ENTITY")    
print(*population)    
        
        
