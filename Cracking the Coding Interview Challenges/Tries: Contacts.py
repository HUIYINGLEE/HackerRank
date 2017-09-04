def add(name, contacts):
    firstLetter=name[0]
    if firstLetter in contacts:
        contacts[firstLetter].append(name)
    else:
        contacts[firstLetter]=[name]
    

def find(name,contacts):
    firstLetter=name[0]
    num=len(name)
    count=0
    if firstLetter not in contacts:
        return 0
    else:
        for s in contacts[firstLetter]:
            if name==s[:num]:
                count+=1
    return count
            
        
        

n = int(input().strip())
contacts={}
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op=="add": add(contact,contacts)
    if op=="find": print(find(contact,contacts))
