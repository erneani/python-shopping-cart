from PrintService import PrintService

class Product:
  def __init__(self, id, name, price, quantity):
    self.print_service = PrintService()
    self.id = id
    self.name = name
    self.price = price
    self.quantity = quantity


  def remove_item(self):
    if (self.quantity > 0):
      self.quantity -= 1
    else:
      self.print_service.out_ouf_items()


  def insert_item(self):
    self.quantity += 1


  def show_product(self):
    self.print_service.show_product(self)

