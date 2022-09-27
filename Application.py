from Product import Product
from ShoppingCart import ShoppingCart
from PrintService import PrintService

class Application:
  def __init__(self):
    self.print_service = PrintService()

    self.is_sale_finished = False
    self.shopping_cart = ShoppingCart()
    self.product_list = self.initialize_products()
    self.sale()


  def initialize_products(self):
    prod_list = [
      Product(1, 'Caneta', 1.30, 3),
      Product(2, 'Caderno', 10, 3),
      Product(3, 'Lápis', 0.5, 3),
      Product(4, 'Borracha', 0.8, 3)
    ]

    return prod_list

  def sale(self):
    while self.is_sale_finished == False:
      self.print_menu()
      self.get_selected_option()


  def get_selected_option(self):
    options = {
      1: self.add_item_to_cart,
      2: self.remove_item_from_cart,
      0: self.finalize_sale,
      9: self.cancel_sale
    }

    selected_option = self.print_service.get_options_to_select()
    if not selected_option in options:
      self.print_service.invalid_option()
    else:
      options[selected_option]()


  def finish_sale(self):
    self.is_sale_finished = True


  def add_item_to_cart(self):
    product_id = self.print_service.get_product_id()

    for item in self.product_list:
      if product_id == item.id:
        if item.quantity > 0:
          item.remove_item()
          self.shopping_cart.add_product(item)
          return
        else:
          self.print_service.product_is_not_available()
          return

    self.print_service.product_not_on_list()


  def remove_item_from_cart(self):
    product_id = self.print_service.get_product_id()

    for item in self.product_list:
      if product_id == item.id:
        if self.shopping_cart.remove_product(item):
          item.insert_item()
        
        return
      
    self.print_service.product_not_on_list()


  def finalize_sale(self):
    self.shopping_cart.finalize()
    self.finish_sale()


  def cancel_sale(self):
    self.shopping_cart.cancel()
    self.finish_sale()


  def print_menu(self):
    self.print_service.print_products_available()
    for item in self.product_list:
      item.show_product()
    self.print_service.empty_line()
  
