import os.path

from csv_parsing.csv_importer import CsvCurrenciesImporter
from models.currencies_exchange import CurrenciesExchange
from models.currency_builder import CurrencyBuilder


def clearConsole():
    print("\n" * 20)  # remove the brackets in Python 2.x


def __printMenu():
    print("\n" * 2)
    print("Actions:")
    print()
    print("[1] - Import currencies from CSV file")
    print("[2] - Define new currency with exchange rates")
    print("[3] - Get all currencies exchange rates in a form of table")
    print("[4] - Check exchange rate between two currencies")
    print("[5] - Exit")


def __filenameRequest():
    filename = input("please provide name of csv file in app_sample_data: ")
    delimiter = input("please provide delimiter")
    return filename, delimiter


def __importCurrenciesFromFile(filepath, delimiter):
    csvCurrencyImporter = CsvCurrenciesImporter()
    csvCurrencyImporter.fill_data_from_csv(filepath, delimiter)
    return csvCurrencyImporter


def __print_currency_exchange(currency, currenciesNames):
    print(currency + ":")
    for curr in currenciesNames:
        print(curr + ":" + str(currenciesExchange.get_exchange_rate(currency, curr)), end='; ')
    print()


def __print_currencies_exchange():
    currenciesNames = currenciesExchange.get_currencies_names()
    if len(currenciesNames) == 0:
        print("Actually no currency has been provided")
        return
    for currency in currenciesNames:
        __print_currency_exchange(currency, currenciesNames)


def __provide_any_key():
    print()
    # keyboard.sleep()


def __let_user_define_new_currency():
    currencyName = input("provide name for your currency")
    while True:
        mainExchangeCurrency = input("provide currency name for evaluating not provided exchange rates")
        if mainExchangeCurrency in currenciesExchange.get_currencies_names():
            break
        print("you've provided unknown currency name")

    currencyBuilder = CurrencyBuilder()
    currencyBuilder.set_name(currencyName)
    mainExchangeCurrencyExchangeRate = float(input("please provide exchange rate for main exchange currency"))
    currencyBuilder.add_currency(mainExchangeCurrency, mainExchangeCurrencyExchangeRate)

    while True:
        print("press x - if you want to add new exchange rate")
        userDecision = input("press ENTER otherwise")
        if userDecision.__eq__("x"):
            currencyExchangeName = __infinitely_ask_for_valid_currency_name()
            currencyExchangeRate = float(input("provide exchange rate for given currency"))
            currencyBuilder.add_currency(currencyExchangeName, currencyExchangeRate)
        else:
            break

    newCurrency = currencyBuilder.build()
    currenciesExchange.add_currency(newCurrency, mainExchangeCurrency)
    print("thank you for providing new currency")
    __print_currency_exchange(currencyName, currenciesExchange.get_currencies_names())


def __infinitely_ask_for_valid_currency_name():
    while True:
        currencyExchangeName = input("print name of currency ")
        names = currenciesExchange.get_currencies_names()
        if currencyExchangeName in names:
            break
        print("you provided unknown currency - try again")
    return currencyExchangeName


def __let_user_check_exchange_rate_beetween_two_currencies():
    print("provide source currency name")
    sourceCurrencyName = __infinitely_ask_for_valid_currency_name()

    print("provide destination currency name")
    while True:
        secondCurrencyName = __infinitely_ask_for_valid_currency_name()
        if secondCurrencyName.__eq__(sourceCurrencyName):
            print(f'exchange rate from {sourceCurrencyName} to {secondCurrencyName} is 1.0')
        else:
            break

    print("exchange rate from {0} to {1} is {2}".format(sourceCurrencyName, secondCurrencyName, str(
        currenciesExchange.get_exchange_rate(sourceCurrencyName, secondCurrencyName))))


def __infinitely_ask_for_valid_csv_filename_and_delimiter():
    while True:
        (filename, delimiter) = __filenameRequest()
        current_directory = os.path.dirname(os.path.abspath(__file__))
        test_path = os.path.join(current_directory, 'app_sample_data', filename)
        test_path = os.path.abspath(test_path)
        if os.path.exists(test_path):
            break
        else:
            print("there is no file " + filename + " in folder app_sample_data - try again?")

    return test_path, delimiter


def __infinitely_ask_for_action_from_menu():
    while True:
        try:
            userInput = int(input("provide your choice"))
        except ValueError:
            print("Not an integer! Try again.")
            __provide_any_key()
            __printMenu()
            continue
        else:
            return userInput


currenciesExchange = CurrenciesExchange()

while True:
    __printMenu()
    userAction = __infinitely_ask_for_action_from_menu()

    if userAction == 5:
        print("you've provided " + str(userAction) + " -  Good Bye")
        break

    if userAction == 1:
        (filename, delimiter) = __infinitely_ask_for_valid_csv_filename_and_delimiter()

        csvCurrencyImporter = __importCurrenciesFromFile(filename, delimiter)
        default_currency = csvCurrencyImporter.get_currencies_names()[0]
        currenciesExchange.add_currencies(csvCurrencyImporter.get_currencies_list(), default_currency)
        __print_currencies_exchange()

    elif userAction == 2:
        __let_user_define_new_currency()

    elif userAction == 3:
        __print_currencies_exchange()

    elif userAction == 4:
        __let_user_check_exchange_rate_beetween_two_currencies()

    else:
        print("you've provided unknown command number - try again")

    __provide_any_key()
