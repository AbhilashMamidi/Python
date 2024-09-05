import requests

def free_api_random_products():
    url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches"
    response = requests.get(url)

    # Convert response to JSON
    data = response.json()

    # Validate success and presence of "data"
    if data.get("success") and "data" in data:
        product_list = data["data"]["data"]  # Access the product list correctly

        # Extract necessary details from each product
        products = []
        for product in product_list:
            productdetails = {
                "category": product["category"],
                "price": product["price"],
                "thumbnail": product["thumbnail"]
            }
            producttitle = product["title"]
            productid = product["id"]
            
            # Store the extracted details
            products.append({
                "productdetails": productdetails,
                "producttitle": producttitle,
                "productid": productid
            })
        
        # Return the list of extracted product details
        return products
    else:
        raise Exception("Failed to fetch the product details")

def main():
    try:
        products = free_api_random_products()
        for product in products:
            print(f"Product details: {product['productdetails']}, "
                  f"Product title: {product['producttitle']}, "
                  f"Product ID: {product['productid']}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
