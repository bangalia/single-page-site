class Coffee:
  
   def __init__(self, name, price):
      self.name = name
      self.price = price

latte = Coffee("Latte", 3.99)
latte.has_milk = True
del latte.price

print(latte.__dict__)