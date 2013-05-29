import re

class RISearchBuilder(object):

    def __init__(self):
        """RISearcher initializer"""
        super(RISearchBuilder, self).__init__()
        self.select_parameters = set()
        self.and_clauses = set()
        self.or_clauses = set()
        self._order_by = None

    def and_clause(self, clause):
        """Add an additional AND clause"""
        self.and_clauses.add(clause)
        return self

    def or_clause(self, clause):
        """Add an additional OR clause"""
        self.or_clauses.add(clause)
        return self

    def order_by(self, variable):
        self._order_by = variable
        return self

    def serialize(self, joiner=" "):
        """Convert object to a string"""
        stringList = []
        stringList.append("select %s" % self.__all_selects())
        stringList.append("from <#ri>")
        stringList.append("where")
        if self.and_clauses:
            stringList.append(self.__all_ands())
        if self.or_clauses:
            stringList.append(self.__all_ors())
        if self._order_by:
            stringList.append("order by %s" % self._order_by)
        return joiner.join(stringList)

    def __all_clauses_tokens(self):
        return " ".join(set(self.__all_clauses().split(' ')))

    def __all_clauses(self):
        return " ".join(self.and_clauses | self.or_clauses)

    def __all_selects(self):
        regex = re.compile("(\$\w+)")
        return " ".join(regex.findall(self.__all_clauses_tokens()))

    def __all_ands(self):
        return " and ".join(self.and_clauses)

    def __all_ors(self):
        temp_ors = ""
        if self.or_clauses:
            temp_ors = " or ".join(self.or_clauses)
            if self.and_clauses:
                temp_ors = "or " + temp_ors
        return temp_ors

