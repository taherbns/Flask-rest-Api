import requests


BASE_URL = "http://127.0.0.1:5000"
TOKEN = "mysecrettoken"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

def test_create_order(order_id, product_name, quantity, price, order_date):
    url = f"{BASE_URL}/order/{order_id}"
    data = {
        "product_name": product_name,
        "quantity": quantity,
        "price": price,
        "order_date": order_date
    }
    response = requests.put(url, headers=HEADERS, json=data)
    print("Create Order:", response.json())

def test_get_order(order_id):
    url = f"{BASE_URL}/order/{order_id}"
    response = requests.get(url, headers=HEADERS)
    print("Get Order:", response.json())

def test_update_order(order_id, product_name=None, quantity=None, price=None, order_date=None):
    url = f"{BASE_URL}/order/{order_id}"
    data = {}
    if product_name:
        data["product_name"] = product_name
    if quantity:
        data["quantity"] = quantity
    if price:
        data["price"] = price
    if order_date:
        data["order_date"] = order_date

    response = requests.patch(url, headers=HEADERS, json=data)
    print("Update Order:", response.json())

def test_delete_order(order_id):
    url = f"{BASE_URL}/order/{order_id}"
    response = requests.delete(url, headers=HEADERS)
    print("Delete Order:", response.json())

def test_search_orders(product_name):
    url = f"{BASE_URL}/ordersearch/{product_name}"
    response = requests.get(url, headers=HEADERS)
    print("Search Orders:", response.json())

if __name__ == "__main__":
   
    test_create_order(1, "Produit B", 10, 100.0, "2024-08-12")

   
    test_get_order(1)

    
    test_update_order(1, quantity=15, price=150.0)

    
    test_search_orders("Produit A")

    
    test_delete_order(1)
