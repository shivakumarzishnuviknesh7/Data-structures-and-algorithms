def simpleFunction():
    stock = [1, 2, 2, 1, 4, 3, 2, 3, 4]
    for i in range(len(stock[1:])):
        print(f"day{i} returns is {stock[i + 1] - stock[i]} profits")

simpleFunction()
print("##############################################################")

def profitEvaluvatorFunction(stock):

    #this methos is used to evaluvate the client profit in daily basis

    for i in range(len(stock[1:])):
        print(f"day{i} returns is {stock[i + 1] - stock[i]} profits")

profitEvaluvatorFunction(stock = [1, 2, 2, 1, 4, 3, 2, 3, 4])


@override
localhost8080/client/asset/gains/profitEvaluvatorFunction
end point is get/profitEvaluvatorFunction(stock)
profitEvaluvatorFunction()interface
to show up

