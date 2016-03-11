class ProductPrice(object):
    def __init__(self, data):
        if 'years' in data: self.years = data['years']
        if 'price' in data: self.price = data['price']
        if 'priceExtra' in data: self.priceExtra = data['priceExtra']
        if 'priceExtraWildcard' in data: self.priceExtraWildcard = data['priceExtraWildcard']