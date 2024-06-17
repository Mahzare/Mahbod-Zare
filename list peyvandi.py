def insert(self, coef, power):
    self.n +=1
    x = self.head.next
    while x != self.head and x.power > power:
        x = x.next
        self.insert_after(xprev, coef, power)

def get(self, ind):
    if ind >= self.size():
      raise exception("out of list")
        x = self.head.next
        for i in range (ind):
        x = x.next
        return f"coef : {x.coef}, power : {x.power}"
