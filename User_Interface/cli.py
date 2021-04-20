from copy import deepcopy
from Logic.validation import dictValidation, dateValidation, valueValidation, aptValidation


def commandCLI(code,spendingsList):
    '''
    This function creates the Command line interface
    :return: -
    '''
    args = code.split(" ")
    if args[0] in ["add", "modify", "delete", "delvalues", "addvalue",
                   "determinate", "order", "monthlysums", "help"]:
        if args[0] == "add":
            from Domain.define import createSpending, addSpending
            from User_Interface.CliParser import addParser
            argument = addParser(args[1:len(args)])
            if argument is not None and dictValidation(argument) and dateValidation(argument['date']) \
                    and valueValidation(argument['value']) and aptValidation(argument['apartment']):
                if argument['type'] == 'alte':
                    spending = createSpending(argument['apartment'], argument['value'], argument['date'],
                                              argument['type'] + ' cheltuieli')
                    addSpending(spending, spendingsList)
                else:
                    spending = createSpending(argument['apartment'], argument['value'], argument['date'],
                                              argument['type'])
                    addSpending(spending, spendingsList)
            else:
                print("Parametrii invalizi")
        if args[0] == "modify":
            from Domain.define import modifySpending
            from User_Interface.CliParser import modifyParser
            argument = modifyParser(args[1:len(args)])
            if argument is not None and dictValidation(argument) and dateValidation(argument['date']) \
                    and valueValidation(argument['value']) and aptValidation(argument['apartment']):
                if argument['type'] == 'alte':
                    modifySpending(spendingsList, argument['apartment'], argument['value'], argument['date'],
                                   argument['type'] + ' cheltuieli')
                else:
                    modifySpending(spendingsList, argument['apartment'], argument['value'], argument['date'],
                                   argument['type'])
            else:
                print("Parametrii invalizi")
        if args[0] == "delete":
            from Domain.define import removeSpending
            from User_Interface.CliParser import deleteParser
            argument = deleteParser(args[1:len(args)])
            if argument is not None and dictValidation(argument) and aptValidation(argument['apartment']):
                removeSpending(argument['apartment'], spendingsList)
            else:
                print("Parametrii invalizi")
        if args[0] == "delvalues":
            from Logic.delete_spendings import delAllSpendings
            from User_Interface.CliParser import delAllParser
            argument = delAllParser(args[1:len(args)])
            if argument is not None and dictValidation(argument) and aptValidation(argument['apartment']):
                delAllSpendings(argument['apartment'], spendingsList)
            else:
                print("Parametrii invalizi")
        if args[0] == "addvalue":
            from Logic.add_to_date import addValToDate
            from User_Interface.CliParser import addValParser
            argument = addValParser(args[1:len(args)])
            if argument is not None and dictValidation(argument) and dateValidation(argument['date'])\
                    and valueValidation(argument['value']):
                addValToDate(argument['date'], argument['value'], spendingsList)
            else:
                print("Parametrii invalizi")
        if args[0] == "determinate":
            from Logic.max_spendings import maxSpending
            print("Pentru cheltuieli de intretinere, valoarea maxima este: ", maxSpending(spendingsList, "intretinere"))
            print("Pentru cheltuieli de canal, valoarea maxima este: ", maxSpending(spendingsList, "canal"))
            print("Pentru alte cheltuieli,valoarea maxima este: ", maxSpending(spendingsList, "alte cheltuieli"))
        if args[0] == "order":
            from Logic.descending_order import orderDescending
            orderDescending(spendingsList)
        if args[0] == "monthlysums":
            from Logic.monthlySums import monthlySums
            monthlyTotal = monthlySums(spendingsList)
            print(*monthlyTotal)
        if args[0] == "help":
            helpCLI()


def helpCLI():
    '''
    This function creates the helper menu for the CLI
    :return: -
    '''
    print("Functiile permise sunt : ")
    print("add [-h, --help] <apartment> <value> <date> <type>  -- adauga un apartment nou in lista de cheltuieli")
    print("modify [-h, --help] <apartment> <value> <date> <type>  "
          "-- modifica cheltuielile unui apartament deja in lista")
    print("delete [-h, --help] <apartment>  -- sterge un apartament")
    print("delvalues [-h, --help] <apartment>  -- sterge toate cheltuielile unui apartament")
    print("addvalue [-h, --help] <date> <value>  -- adauga o valoare la toate cheltuielile dintr-o data anume")
    print("determinate [-h, --help] -- determina cele mai mare cheltuieli dupa tipul lor")
    print("order [-h, --help] -- ordoneaza lista descrescator dupa valoarea cheltuielii")
    print("monthlysums [-h, --help] -- afiseaza sumele lunare ale fiecarui apartament")
    print("undo [-h, --help] -- anuleaza ultima actiune")
    print("exit [-h, --help] -- iesi din CLI")
    print("help -- afiseaza toate functiile programului")


def runCLI(spendingsList):
    '''
    This function runs the CLI
    :return:
    '''
    code = input("Introduceti codul dorit: ")
    stack = []
    while code != 'exit':
        args = code.split(";")
        for index in range(len(args)):
            value = args[index]
            commandCLI(value, spendingsList)
            if value not in ['undo', 'showlist', 'help']:
                stack.append(deepcopy(spendingsList))
            if value == "undo":
                if stack:
                    stack.pop()
                    if stack:
                        spendingsList = stack[-1]
                    else:
                        spendingsList = []
                else:
                    print("Nu aveti ce actiune sa anulati")
            if value == "showlist":
                if stack:
                    print(stack[-1])
                else:
                    print('Lista goala')
        code = input("Introduceti codul dorit: ")
