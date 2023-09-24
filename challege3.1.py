def linearsearchproducts(productslist,targetproducts):
    indices=[]
    for index,product in enumerate(productslist):
        if product==targetproducts:
            indices.append(index)
    return indices

products=["yamaha","ktm","honda","bajaj pulsar","ktm"]
target="ktm"
final=linearsearchproducts(products,target)
print(final)