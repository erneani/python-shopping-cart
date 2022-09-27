class PrintService:
  def get_options_to_select(self):
    print('O que deseja fazer?')
    print('1 - Adicionar um item')
    print('2 - Remover um item')
    print('0 - Finalizar compra')
    print('9 - Cancelar compra')
    return int(input())


  def print_products_available(self):
    self.empty_line()
    print('Produtos disponíveis para compra: ')


  def empty_line(self):
    print()


  def get_product_id(self):
    print('Insira o ID do produto:')
    return int(input())

  
  def product_not_on_list(self):
    self.empty_line()
    print('Produto não está na lista')
    self.empty_line()


  def product_is_not_available(self):
    self.empty_line()
    print('Não há mais produtos disponíveis')
    self.empty_line()


  def no_items_found(self):
    self.empty_line()
    print('Não há nenhum item desse tipo')


  def finaliza_sale_description(self, total_value, products):
    print('--------- Descrição da compra ---------')
    self.print_products_recipe(products)
    print(f'Valor total - R${total_value:.2f}')
  

  def cancel_sale_description(self, products):
    print('--------- Cancelamento da compra ---------')
    self.print_products_recipe(products)

  
  def print_products_recipe(self, products_to_print):
    for item in products_to_print:
      print(f'{item.quantity}x {item.name} - R${(item.price * item.quantity):.2f}')
  

  def show_product(self, product):
    print(f'{product.id} | {product.quantity}x {product.name} - R${product.price:.2f}')
  

  def out_ouf_items(self):
    self.empty_line()
    print('Não há mais itens com esse ID')

  def invalid_option(self):
    self.empty_line()
    print('Opção inválida')