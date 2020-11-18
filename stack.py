# implementing stack using list 

class stack:
    def __init__(self,limit):
        self.top = -1
        self.limit = limit
        self.stack = list ()
    def push (self,val):
        if self.top < self.limit:
            self.stack.append(val)
            self.top += 1
        else:
            return "Stack overflow"
    def pop ():
        if self.top > 0:
            val = self.stack [self.top]
            self.top -= 1
            return val
        else:
            return "Stack underflow"
    def show (self):
        return {self.top:self.stack}
if __name__ =="__main__":
    limit = input ("Enter the size of stack :")
    stk = stack (int (limit))
    while True:
        print ("Stack DS\n")
        print ("\t1. Show stack.")
        print ("\t2. Push to stack.")
        print ("\t3. Pop from stack.")
        opt = input ("\n Enter option : ")
        opt = int (opt)
        if opt == 1:
            print (stk.show ())

        if opt == 2:
            val = input ("Enter the value :")
            print ("Pushing ",val)
            stk.push (int (val))
            print ("Pushed")
        if opt == 3:
            print ("Popping")
            val = stk.pop ()
            print ("Popped : ",val)
        if input ("press ^d to stop"):
            break






