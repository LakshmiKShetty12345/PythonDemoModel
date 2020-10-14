ItemInCart = 0

if ItemInCart != 3:#raise Exception("Product cart count is not equal")
    pass

assert(ItemInCart == 0)

#try,catch
try:
    with open("Tes.txt","r") as reader:
        reader.read()

except Exception as e:
    print(e)
finally:
    print("Cleaning up resourse")

