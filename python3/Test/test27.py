#โปรแกรมหาเลขคู่เลขคี่แบบใช้ functions

def odd_even(x):
    if x%2 == 0:
        print("เป็นเลขคู่",x)
    else:
        print("เป็นเลขคี่",x)
a,b,c,d = 10,2,44,3
odd_even(a)