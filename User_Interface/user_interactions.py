from User_Interface.menu import menu
from Logic.validation import *
from copy import deepcopy


def userInterface(spendingsList):
    '''
    This function creates the enviroment for user interactions
    :param spendingsList: - list - the list that contains all the spendings
    :return: -
    '''
    option = menu()
    stack = []
    while option != 'stop':
        if representsInt(option):
            option = int(option)
            if option == 1:
                print("Ati ales sa adaugati o noua cheltuiala")
                apartNumber = input("Introduceti numarul apartamentului: ")
                while not aptValidation(apartNumber):
                    apartNumber = input("Introduceti un numar valid pentru apartament: ")
                apartNumber = int(apartNumber)
                value = input("Introduceti valoarea cheltuielii: ")
                while not valueValidation(value):
                    value = input("Introduceti o valoare valida pentru cheltuiala: ")
                value = float(value)
                date = input("Introduceti data cheltuielii: ")
                while not dateValidation(date):
                    date = input("Introduceti o valoare valida pentru data: ")
                typeS = input("Introduceti tipul cheltuielii: ")
                while not typeValidation(typeS):
                    typeS = input("Introduceti un tip valid pentru cheltuieala: ")
                from Domain.define import createSpending, addSpending
                spending = createSpending(apartNumber, value, date, typeS)
                addSpending(spending, spendingsList)
                stack.append(deepcopy(spendingsList))
            elif option == 2:
                print("Ati ales sa modificati o cheltuiala")
                if len(spendingsList) != 0:
                    apartNumber = input("Introduceti numarul apartamentului: ")
                    while not aptValidation(apartNumber):
                        apartNumber = input("Introduceti un numar valid pentru apartament: ")
                    apartNumber = int(apartNumber)
                    value = input("Introduceti valoarea cheltuielii: ")
                    while not valueValidation(value):
                        value = input("Introduceti o valoare valida pentru cheltuiala: ")
                    value = float(value)
                    date = input("Introduceti data cheltuielii: ")
                    while not dateValidation(date):
                        date = input("Introduceti o valoare valida pentru data: ")
                    typeS = input("Introduceti tipul cheltuielii: ")
                    while not typeValidation(typeS):
                        typeS = input("Introduceti un tip valid pentru cheltuieala: ")
                    from Domain.define import modifySpending
                    modifySpending(spendingsList, apartNumber, value, date, typeS)
                    stack.append(deepcopy(spendingsList))
                else:
                    print("Introduceti intai valori in lista cheltuielilor")
            elif option == 3:
                print("Ati ales sa stergeti o cheltuiala")
                if len(spendingsList) != 0:
                    apartNumber = input("Introduceti numarul apartamentului: ")
                    while not aptValidation(apartNumber):
                        apartNumber = input("Introduceti un numar valid pentru apartament: ")
                    apartNumber = int(apartNumber)
                    from Domain.define import removeSpending
                    removeSpending(apartNumber, spendingsList)
                    stack.append(deepcopy(spendingsList))
                else:
                    print("Nu exista valori spre a fi sterse")
            elif option == 4:
                print("Ati ales sa stergeti toate cheltuielile pentru un apartament dat")
                if len(spendingsList) != 0:
                    apartNumber = input("Introduceti numarul apartamentului: ")
                    while not aptValidation(apartNumber):
                        apartNumber = input("Introduceti un numar valid pentru apartament: ")
                    apartNumber = int(apartNumber)
                    from Logic.delete_spendings import delAllSpendings
                    delAllSpendings(apartNumber, spendingsList)
                    stack.append(deepcopy(spendingsList))
                else:
                    print("Nu exista valori spre a fi sterse")
            elif option == 5:
                print("Ati ales sa adaugati o valoare la toate cheltuielile dintr-o anumita data")
                if len(spendingsList) != 0:
                    date = input("Introduceti data cheltuielii: ")
                    while not dateValidation(date):
                        date = input("Introduceti o valoare valida pentru data: ")
                    value = input("Introduceti valoarea cheltuielii: ")
                    while not valueValidation(value):
                        value = input("Introduceti o valoare valid pentru cheltuieala: ")
                    value = float(value)
                    from Logic.add_to_date import addValToDate
                    addValToDate(date, value, spendingsList)
                    stack.append(deepcopy(spendingsList))
                else:
                    print("Introduceti intai valori in lista cheltuielilor")
            elif option == 6:
                print("Ati ales sa determinati cea mai mare valoare pentru fiecare tip")
                if len(spendingsList) != 0:
                    from Logic.max_spendings import maxSpending
                    print("Pentru cheltuieli de intretinere, valoarea maxima este: ", maxSpending(spendingsList, "intretinere"))
                    print("Pentru cheltuieli de canal, valoarea maxima este: ", maxSpending(spendingsList, "canal"))
                    print("Pentru alte cheltuieli,valoarea maxima este: ", maxSpending(spendingsList, "alte cheltuieli"))
                    stack.append(deepcopy(spendingsList))
                else:
                    print("Introduceti intai valori in lista cheltuielilor")
            elif option == 7:
                print("Ati ales sa ordonati descrescator cheltuielile dupa suma")
                if len(spendingsList) != 0:
                    from Logic.descending_order import orderDescending
                    orderDescending(spendingsList)
                    stack.append(deepcopy(spendingsList))
                else:
                    print("Introduceti intai valori in lista cheltuielilor")
            elif option == 8:
                print("Ati ales sa afisati sumele lunare pentru fiecare apartament")
                if len(spendingsList) != 0:
                    from Logic.monthlySums import monthlySums
                    monthlyTotal = monthlySums(spendingsList)
                    print(*monthlyTotal)
                    stack.append(deepcopy(spendingsList))
                else:
                    print("Introduceti intai valori in lista cheltuielilor")
            elif option == 9:
                if stack:
                    stack.pop()
                    if stack:
                        spendingsList=stack[-1]
                    else:
                        spendingsList = []
                else:
                    print("Nu aveti ce actiune sa anulati")
            elif option == 10:
                from User_Interface.cli import runCLI
                runCLI(spendingsList)
            else:
                print("Introduceti una dintre optiunile valide sau stop pentru a opri programul")
        else:
            print("Introduceti una dintre optiunile valide sau stop pentru a opri programul")
        if stack:
            print(stack[-1])
        option = menu()

