class Influencer:
    def __init__(self, username, followers):
        self.username = username
        self.followers = followers

class Brand:
    def __init__(self, brand_name):
        self.brand_name = brand_name

class BrandPartner(Influencer, Brand):
    def __init__(self, username, followers, brand_name):
        Influencer.__init__(self, username, followers)
        Brand.__init__(self, brand_name)

obj = BrandPartner("ramesh", 25000, "Nike")

print(obj.username)
print(obj.followers)
print(obj.brand_name)