import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_villa.settings")
django.setup()

from villApp.models import Product

def create_sample_products():
    products = [
        {"name": "Ring", "price": 200.00, "description": "Beautiful silver ring"},
        {"name": "Watch", "price": 300.00, "description": "Elegant wrist watch"},
        {"name": "Teddy Bear", "price": 110.00, "description": "Soft and cuddly teddy bear"},
        {"name": "Flower Bouquet", "price": 45.00, "description": "Fresh flowers"},
    ]

    for p in products:
        Product.objects.get_or_create(name=p["name"], defaults=p)
        print(f"Created/Checked product: {p['name']}")

if __name__ == "__main__":
    create_sample_products()
