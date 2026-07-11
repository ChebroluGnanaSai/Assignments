categories=2
num_products=3
entry={}
for i in range(categories):
    category = input("Enter a category: ")
    product_list=[]
    for j in range(num_products):
        product=input(f"Enter Product {j+1} under {category}: ")
        stock=int(input(f"Enter available stock for {product}: "))
        product_list.append({
            "Product": product,
            "Available Stock": stock
        })
    entry[category]=product_list
print("\nAvailable Stock")
for category,product_list in entry.items():
    print(f"\nCategory: {category}")
    for item in product_list:
        print(f"Product: {item['Product']}, Available Stock: {item['Available Stock']}")
