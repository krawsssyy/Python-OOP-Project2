def menu():
    '''
    This function creates the user menu
    :return: option - string - the selected operation by the user
    '''
    print("1.Adaugati cheltuiala")
    print("2.Modificati cheltuiala")
    print("3.Stergeti cheltuiala")
    print("4.Stergeti toate cheltuielile pentru un apartament dat")
    print("5.Adunati o valoarea la cheltuielile de la o data anume")
    print("6.Determinati cea mai mare cheltuiala dupa tip")
    print("7.Ordonati cheltuielile descrescator")
    print("8.Obtineti sumele lunare pentru fiecare apartament")
    print("9.Undo")
    print("10.Intrati in interfata unei linii de comanda")
    option = input("Introduceti optiunea dorita: ")
    return option