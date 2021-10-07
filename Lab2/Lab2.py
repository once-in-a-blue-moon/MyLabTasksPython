x = float(input('Enter x: '))
y = float(input('Enter y: '))
circle = x*x + y*y
result_pos = "Точка (x,y) належить заштрихованiй частинi площини";
result_neg = "Точка (x,y) не належить заштрихованiй частинi площини";
if(circle<=4):

    if(x >= 0 and y >= 0 and x + y >= 2):
        print(result_pos)
    elif(x >= 0 and y < 0 and -x + y >= -2):
        print(result_pos)
    elif(x < 0 and y >= 0 and -x + y <= -2):
        print(result_pos)
    elif(x < 0 and y < 0 and x + y <= -2):
        print(result_pos)
    else: print(result_neg)

else: print(result_neg)

