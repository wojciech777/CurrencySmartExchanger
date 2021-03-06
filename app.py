import os.path

from csv_parsing.csv_importer import CsvCurrenciesImporter
from models.currencies_exchange import CurrenciesExchange
from models.currency_builder import CurrencyBuilder
from network_service.nbp_service_proxy import NBPServiceProxy


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
    print("[5] - Check NBP currencies and exchange rates")
    print("[6] - Exit")


def __filenameRequest():
    filename = input("Please provide name of csv file in app_sample_data: ")
    delimiter = input("Please provide delimiter: ")
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
        print("Actually, no currency has been provided")
        return
    for currency in currenciesNames:
        __print_currency_exchange(currency, currenciesNames)


def __provide_any_key():
    print()
    dump = input("press ENTER to continue")


def __let_user_define_new_currency():
    currencyName = input("Provide name for your currency")
    while True:
        mainExchangeCurrency = input("Provide currency name for evaluating not provided exchange rates: ")
        if mainExchangeCurrency in currenciesExchange.get_currencies_names():
            break
        print("You've provided unknown currency name")

    currencyBuilder = CurrencyBuilder()
    currencyBuilder.set_name(currencyName)
    mainExchangeCurrencyExchangeRate = float(input("Please provide exchange rate for main exchange currency: "))
    currencyBuilder.add_currency(mainExchangeCurrency, mainExchangeCurrencyExchangeRate)

    while True:
        print("P x - if you want to add new exchange rate ")
        userDecision = input("Press ENTER otherwise ")
        if userDecision.__eq__("x"):
            currencyExchangeName = __infinitely_ask_for_valid_currency_name()
            currencyExchangeRate = float(input("Provide exchange rate for given currency: "))
            currencyBuilder.add_currency(currencyExchangeName, currencyExchangeRate)
        else:
            break

    newCurrency = currencyBuilder.build()
    currenciesExchange.add_currency(newCurrency, mainExchangeCurrency)
    print("New currency added")
    __print_currency_exchange(currencyName, currenciesExchange.get_currencies_names())


def __infinitely_ask_for_valid_currency_name():
    while True:
        currencyExchangeName = input("Provider name of the currency: ")
        names = currenciesExchange.get_currencies_names()
        if currencyExchangeName in names:
            break
        print("You have provided unknown currency - try again")
    return currencyExchangeName


def __infinitely_ask_for_valid_currency_type():
    while True:
        currencyExchangeType = input("Provide currency type (A, B, C): ")
        types = ["A", "a", "B", "b", "C", "c"]
        if currencyExchangeType in types:
            break
        print("You have provided unknown type - try again")
    return currencyExchangeType


def __let_user_check_exchange_rate_beetween_two_currencies():
    print("Provide source currency name: ")
    sourceCurrencyName = __infinitely_ask_for_valid_currency_name()

    print("Provide destination currency name: ")
    while True:
        secondCurrencyName = __infinitely_ask_for_valid_currency_name()
        if secondCurrencyName.__eq__(sourceCurrencyName):
            print(f'Exchange rate from {sourceCurrencyName} to {secondCurrencyName} is 1.0')
        else:
            break

    print("Exchange rate from {0} to {1} is {2}".format(sourceCurrencyName, secondCurrencyName, str(
        currenciesExchange.get_exchange_rate(sourceCurrencyName, secondCurrencyName))))


def __let_user_check_exchange_rate_nbp():
    source_currency_type = __infinitely_ask_for_valid_currency_type()

    nbp_service = NBPServiceProxy()
    if source_currency_type == "A" or source_currency_type == "a":
        network_currencies = nbp_service.getCurrenciesCategoryA()
    elif source_currency_type == "B" or source_currency_type == "b":
        network_currencies = nbp_service.getCurrenciesCategoryB()
    else:
        network_currencies = nbp_service.getCurrenciesCategoryC()

    for currency in network_currencies:
        print("{0} - {1} - rate {2}".format(currency.get_code(),
                                            currency.get_currency(),
                                            str(currency.get_mid())))


def __infinitely_ask_for_valid_csv_filename_and_delimiter():
    while True:
        (filename, delimiter) = __filenameRequest()
        current_directory = os.path.dirname(os.path.abspath(__file__))
        test_path = os.path.join(current_directory, 'app_sample_data', filename)
        test_path = os.path.abspath(test_path)
        if os.path.exists(test_path):
            break
        else:
            print("There is no file " + filename + " in folder app_sample_data")
            print("if you want to try to provide another csv filename - press y and commit by ENTER ")
            command = input("otherwise - press any key different from y ")
            if command.__eq__("y"):
                continue
            else:
                raise Exception

    return test_path, delimiter


def __infinitely_ask_for_action_from_menu():
    while True:
        try:
            userInput = int(input("Your choice: "))
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

    if userAction == 6:
        print("You've provided " + str(userAction) + " -  Good Bye")
        break

    if userAction == 1:
        user_withdrawn = False
        try:
            (filename, delimiter) = __infinitely_ask_for_valid_csv_filename_and_delimiter()
        except Exception:
            print("you've withdrawn from providing csv filename and delimiter")
            user_withdrawn = True

        if not user_withdrawn:
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

    elif userAction == 5:
        __let_user_check_exchange_rate_nbp()

    else:
        print("You've provided unknown command number - try again")

    __provide_any_key()
