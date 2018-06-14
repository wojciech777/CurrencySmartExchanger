class CurrenciesExchange:

    def __init__(self):
        self._currs = []
        self._curr_dict = {}
        self._unkn_currs = []

    def add_currency(self, new_curr, def_exchange_curr):
        for curr in self._currs:
            if not ((def_exchange_curr, curr) in self._curr_dict):
                raise ValueError("This default_exchange_currency can't be used, chose another")
        if not (new_curr.get_name() in self._currs):
            self._currs.append(new_curr.get_name())
        self._curr_dict[new_curr.get_name(), new_curr.get_name()] = 1
        self._unkn_currs = []
        self.__add_new_currency(new_curr)
        self.__update_old_currencies(new_curr, def_exchange_curr)
        for unkn_curr in self._unkn_currs:
            if not (unkn_curr in self._currs):
                self._currs.append(unkn_curr)
        self.__update_unknown_currencies(new_curr)
        self._unkn_currs = []

    def add_currencies(self, currs, def_exchange_curr):
        for curr in currs:
            self.add_currency(curr, def_exchange_curr)

    def get_exchange_rate(self, src_curr, dest_curr):
        return self._curr_dict[src_curr, dest_curr]

    def get_currency_exchange_dictionary(self):
        return self._curr_dict

    def get_currencies_names(self):
        return self._currs

    def __add_new_currency(self, new_curr):
        for exchange_rate in new_curr.get_all_related_currencies_as_list():
            if self._currs.count(exchange_rate.get_name()) == 0:
                self._unkn_currs.append(exchange_rate.get_name())

            self._curr_dict[new_curr.get_name(), exchange_rate.get_name()] = exchange_rate.get_value()
            if not ((exchange_rate.get_name(), new_curr.get_name()) in self._curr_dict):
                self._curr_dict[exchange_rate.get_name(), new_curr.get_name()] = 1 / exchange_rate.get_value()

    def __update_old_currencies(self, new_curr, def_exchange_curr):
        for curr in self._currs:
            if not((new_curr.get_name(), curr) in self._curr_dict):
                self._curr_dict[new_curr.get_name(), curr] = self._curr_dict[
                                                                new_curr.get_name(), def_exchange_curr] * \
                                                             self._curr_dict[
                                                                def_exchange_curr, curr]
                if not ((curr, new_curr.get_name()) in self._curr_dict):
                    self._curr_dict[curr, new_curr.get_name()] = 1 / self._curr_dict[
                        new_curr.get_name(), def_exchange_curr] * self._curr_dict[
                                                                    def_exchange_curr, curr]

    def __update_unknown_currencies(self, new_curr):
        for unkn_curr in self._unkn_currs:
            for curr in self._currs:
                self._curr_dict[unkn_curr, unkn_curr] = 1
                if not((unkn_curr, curr) in self._curr_dict):
                    self._curr_dict[unkn_curr, curr] = self._curr_dict[
                                                                    unkn_curr, new_curr.get_name()] * \
                                                          self._curr_dict[
                                                                    new_curr.get_name(), curr]
                    if not((curr, unkn_curr) in  self._curr_dict):
                        self._curr_dict[curr, unkn_curr] = 1 / self._curr_dict[
                            unkn_curr, new_curr.get_name()] * self._curr_dict[
                                                                new_curr.get_name(), curr]