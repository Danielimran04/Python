import time
# defaault arguments = A default value for certain parameters
#                      default is used when that argument is omitted
#                      make your functions more flexible , reduces # of arguments
#                      1. positional , 2.DEFAULT, 3. keyword , 4.arbitrary

# kalau dlm parameter function declaration nih dh letak value dekat function call boleh masuk nilai baru so contoh line 13 
# dia akan tukar parameter value dekat function line 9

def net_price(list_price,discount=0,tax=0.05):
    return list_price * (1-discount) * (1+tax)


print(net_price(500))
print(net_price(500,0.2,4))

def count(start,end):
    for x in range(start, end +1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(0,10)

def countterbalik(end,start):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

countterbalik(30,15)