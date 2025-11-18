# Boolean Variable that is True
discounted = True
low_in_stock = True

movingProduct = discounted or low_in_stock

promotion = not movingProduct

print("is the item eligible for promotion?", promotion)