from Product import Product
from PrintService import PrintService

class ShoppingCart:
  def __init__(self):
    self.print_service = PrintService()
    self.selected_products = []
    self.total_value = 0.0


  def add_product(self, product):
    for item in self.selected_products:
      if item.id == product.id:
        item.insert_item()
        self.total_value += product.price
    
    if not self.has_item(product.id):
      self.selected_products.append(Product(product.id, product.name, product.price, 1))
      self.total_value += product.price


  def remove_product(self, product):
    if not self.has_item(product.id):
      self.print_service.product_not_on_list()
      return False

    for item in self.selected_products:
      if item.id == product.id:
        item.remove_item()
        self.total_value -= product.price

        if item.quantity == 0:
          self.selected_products.remove(item)
        
        return True


  def finalize(self):
    self.print_service.finaliza_sale_description(self.total_value, self.selected_products)


  def cancel(self):
    self.print_service.cancel_sale_description(self.selected_products)


  def has_item(self, product_id):
    for item in self.selected_products:
      if item.id == product_id:
        return True
    
    return False

