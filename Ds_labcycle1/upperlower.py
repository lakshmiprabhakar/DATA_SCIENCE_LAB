class greeter:
    def __init__(self,name):
        self.name = name
    def greet(self,loud=False):
        if loud:
            print("HELLO",self.name.upper())
        else:
            print("Hello",self.name.lower())
g=  greeter('fred')
g.greet()
g.greet(loud=True)

//OUTPUT___________________________

Hello fred
HELLO FRED
