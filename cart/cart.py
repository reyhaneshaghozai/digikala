from shop.models import Product
class Cart:
    def __init__(self, request ):
        self.session = request.session 

        cart =self.session.get('session_key')
        if 'session_key' not in request.session: 
            cart = self.session['session_key']={}
        self.cart = cart 

    def add(self,product,quantity):
        product_id= str(product.id)
        product_qty= str(quantity)


        if product_id in self.cart:
            pass
        else:   
            self.cart[product_id] = product_qty

        self.session.modified = True 
    
    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        product_ids= self.cart.keys()
        products= Product.objects.filter(id__in=product_ids)
        return products
    
    def get_quants(self):
        quantitis= self.cart
        return quantitis
    
    def get_total(self):
        # {'2':3,'1':1,'6':6}
        Product_ids= self.cart.keys()
        Products= Product.objects.filter(id__in = Product_ids)
        total= 0
        for key,value in self.cart.items():
            key = int(key)
            value=int(value)
            for Productss in Products:
                if Productss.id == key:
                    if Productss.is_sale:
                        total = total + (Productss.sale_price *value)
                    else:
                        total = total + (Productss.price *value)
        return total


    
    def update(self, product_id, quantity):
        product_id = str(product_id)
        product_qty = int(quantity)

        ourcart = self.cart
        ourcart[product_id]=product_qty
        self.session.modified = True

        alaki = self.cart
        return alaki
    
    def delete(self, product ):
        product_id= str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

        