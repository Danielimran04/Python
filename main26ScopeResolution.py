# variable scope = where a variable is visible and accessible 
#                = maksud dia kita tahu other punya function punya value contoh function 1 nak access dekat function 2
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in 

def func1(): # variable a is local to function 1
    a = 1
    print(a)

def func2(): # variable b is local to function 2
    b=2
    print(b)

def func3():# yg nih pulak enclosed 
    x=1
   

    def func4():#dlm func4() nih is local
        x=2
        print(x)

    func4()

func3()# kalau kita buang x kat local function dia akan baca enclosed dia macam urutan dekat line 3 yg aku tulis
# gloval scope pulak is outside dri function
#cth global 

print()
def func5():
    print(x)

def func6():
    print(x)

x=3

func5()
func6()
# kalau dlm func5() and func6() aku letak x cth x=3 dlm dua dua function tersebut dia akan baca dalam function dia tak baca x kat luar function 


