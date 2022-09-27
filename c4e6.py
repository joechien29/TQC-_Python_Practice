height = eval(input())
while height != -9999:

    weight = eval(input())
    bmi = weight / (height / 100) ** 2
    if bmi < 18.5:
        print('BMI:{:.2f}'.format(bmi))
        print('State: under weight')
    elif 18.5 <= bmi < 25:
        print('BMI:{:.2f}'.format(bmi))
        print('State: normal')
    elif 25.0 <= bmi < 30:
        print('BMI:{:.2f}'.format(bmi))
        print('State: over weight')
    elif 30 <= bmi:
        print('BMI:{:.2f}'.format(bmi))
        print('State: fat')
    height = eval(input())
