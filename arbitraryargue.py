#Create a function named 'calculate_product' that receives an arbitrary argument list and returns the product of all the arguments. Call the function with the arguments 10,20 and 30 then with the sequence of integrers produced by range (1,6,2)


def calculate_product(*nums):
    """
    Returns the product of the inputs
    """
    count = len(nums)
    products = 1
    i=0
    while i < count:
        products *= nums[i]
        i += 1
        
    print (products)

#Teacher's code
def calculate_product_t(*args):
    """
    docstring
    """
    product_t = 1
    for value in args:
        product_t *= value
    return product_t

counts = calculate_product(10,20,30,50)
counts_s = calculate_product(*range(1,6,2))

counts_t = calculate_product_t(10,20,30,50)
print (counts_t)
