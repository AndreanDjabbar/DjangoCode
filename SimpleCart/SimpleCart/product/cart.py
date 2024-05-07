from .models import ProductModel

class Cart():
    def __init__(self, request):
        self.session = request.session
        
        cart = self.session.get("session_key")
        # Get the current session key if exist

        if "session_key" not in request.session:
            # If not exist and create one
            cart = self.session["session_key"] = {}
        
        self.cart = cart
    
    def add(self, product, quantity):
        product_id = str(product.id)
        product_quantity = str(quantity)

        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {"price":str(product.product_stock)}
            self.cart[product_id] = int(product_quantity)

        self.session.modified = True

    def get_totals(self):
        product_ids = self.cart.keys()
        products = ProductModel.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0

        for quantity in quantities.values():
            total += quantity
        return total
    
        # for key, value in quantities.items():
        #     key = int(key)
        #     for product in products:
        #         if product.id == key:
        #             total += product.product_stock
        # return total

    def __len__(self):
        return len(self.cart)
    
    def get_products(self):
        product_ids = self.cart.keys()
        products = ProductModel.objects.filter(id__in=product_ids)
        return products
    
    def get_quantities(self):
        quantites = self.cart
        return quantites
    
    def update(self, product, quantity):
        product_id = str(product)
        product_quantity = int(quantity)

        outcart = self.cart
        outcart[product_id] = product_quantity

        self.session.modified = True
        thing = self.cart
        return thing
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True

    def clear_cart(self):
        self.cart.clear()
        self.session.modified = True

    def checkout(self):
        product_ids = self.cart
        for key, value in product_ids.items():
            get_product = ProductModel.objects.get(id=key)
            get_product.product_stock -= value
            get_product.save()
        self.clear_cart()