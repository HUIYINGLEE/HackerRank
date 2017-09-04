class MyQueue(object):
    def __init__(self):
        self.inbox=[]
        self.outbox=[]
    
    def peek(self):
        if len(self.outbox)==0:
            while self.inbox:
                ele=self.inbox.pop()
                self.outbox.append(ele)
        return self.outbox[-1]
        
    def pop(self):
        if len(self.outbox)==0:
            while len(self.inbox)!=0:
                ele=self.inbox.pop()
                self.outbox.append(ele)
        return self.outbox.pop()
        
    def put(self, value):
        self.inbox.append(value)
        
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        
