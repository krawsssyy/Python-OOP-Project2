import argparse


def errorMsg(errmsg):
    '''
    This function is used to overwrite the error function from the argument parser so it doesnt raise an error
    :param errmsg: - error
    :return: -
    '''
    print(errmsg)


def addParser(command):
    '''
    This function is the parser for the add comand of the CLI
    :param command: - string - the command parameters
    :return: - args - dictionary
    '''
    parser = argparse.ArgumentParser(prog="add", description="This function adds a spending")
    parser.add_argument('apartment', type=int, help="The apartment number")
    parser.add_argument('value', type=float, help="The value of the spending")
    parser.add_argument('date', help="The date of the spending")
    parser.add_argument('type', choices=['canal', 'intretinere', 'alte'], help="The type of the spending")
    parser.error = errorMsg
    try:
        args = parser.parse_args(command)
        return vars(args)
    except TypeError as te:
        print(te)


def modifyParser(command):
    '''
    This function is used to create a parser for the modify command
    :param command: - string - the command parameters
    :return: - args - dictionary
    '''
    parser = argparse.ArgumentParser(prog="modify", description="This function modifies a spending")
    parser.add_argument('apartment', type=int, help="The apartment number")
    parser.add_argument('value', type=float, help="The value of the spending")
    parser.add_argument('date', help="The date of the spending")
    parser.add_argument('type', choices=['canal', 'intretinere', 'alte'], help="The type of the spending")
    parser.error = errorMsg
    try:
        args = parser.parse_args(command)
        return vars(args)
    except TypeError as te:
        print(te)


def deleteParser(command):
    '''
    This function is used to create a parser for the delete command of the CLI
    :param command: - string - the command parameters
    :return: - args - dictionary
    '''
    parser = argparse.ArgumentParser(prog="delete",
                                     description="This function deletes a spending from a given apartment")
    parser.add_argument('apartment', type=int, help="The apartment number")
    parser.error = errorMsg
    try:
        args = parser.parse_args(command)
        return vars(args)
    except TypeError as te:
        print(te)


def delAllParser(command):
    '''
    This function is used to create the parser for the delvalues command of the CLI
    :param command: - string - the command parameters
    :return: - args - dictionary
    '''
    parser = argparse.ArgumentParse(prog="delvalues",
                                    description="This function deletes all the spendings from a given apartment")
    parser.add_argument('apartment', type=int, help="The apartment number")
    parser.error = errorMsg
    try:
        args = parser.parse_args(command)
        return vars(args)
    except TypeError as te:
        print(te)


def addValParser(command):
    '''
    This function is used to create the parser for the addvalue command of the CLI
    :param command: - string - the command parameters
    :return: - args - dictionary
    '''
    parser = argparse.ArgumentParse(prog="addvalue",
                                    description="This function deletes all the spendings from a given apartment")
    parser.add_argument('date', help="The date")
    parser.add_argument('value', type=float, help="The value to be added")
    parser.error = errorMsg
    try:
        args = parser.parse_args(command)
        return vars(args)
    except TypeError as te:
        print(te)
