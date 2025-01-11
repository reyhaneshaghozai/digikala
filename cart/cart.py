class Cart:
    def __init__(self, request ):
        self.session = request.session 

        cart =self.session.get('session_key')
        if 'session_key' not in request.session: 
            cart = self.session['session_key']={}

            self.cart = cart 
        def add(self,Product):
            Product_id= str(Product.id)

            if Product_id in self.cart:
                pass
            else:
                self.cart[Product_id] ={'price':str(Product.price)}

                self.session.modified = True