class node:
    def __init__(self,data=None,link=None):
        self.data=data
        self.link=link
    def __str__(self):
        return str(self.data)
    def __repr__(self):
            return str(self.data)
    


node1=node(12)
print(node1)
repr(node1)
