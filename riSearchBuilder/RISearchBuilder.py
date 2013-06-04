import re
from collections import namedtuple

class RITriple(namedtuple('RITripple','subject predicate object')):

    def __str__(self):
        return "%s %s %s" % (self.subject, self.predicate, self.object)

class RISearchBuilder(object):

    def __init__(self):
        """RISearcher initializer"""
        super(RISearchBuilder, self).__init__()
        self._and_clauses = set()
        self._or_clauses = set()
        self._order_by = None

    def and_clause(self, clause):
        """Add an additional AND clause"""
        self._and_clauses.add(clause)
        return self

    def or_clause(self, clause):
        """Add an additional OR clause"""
        self._or_clauses.add(clause)
        return self

    def _get_order_by(self):
        return self._order_by

    def order_by(self, variable):
        self._order_by = variable
        return self

    def serialize(self, joiner=" "):
        """Convert object to a string"""
        stringList = []
        stringList.append("select %s" % self._all_selects())
        stringList.append("from <#ri>")
        stringList.append("where")
        if self._and_clauses:
            stringList.append(self._all_ands())
        if self._or_clauses:
            stringList.append(self._all_ors())
        if self._get_order_by() and self._get_order_by() in self._all_selects().split(" "):
            stringList.append("order by %s" % self._get_order_by())
        return joiner.join(stringList)

    def _all_clauses_tokens(self):
        return " ".join(set(self._all_clauses().split(' ')))

    def _all_clauses(self):
        return " ".join(map(str, self._and_clauses | self._or_clauses))

    def _all_selects(self):
        regex = re.compile("(\$\w+)")
        return " ".join(regex.findall(self._all_clauses_tokens()))

    def _all_ands(self):
        return " and ".join(map(str,self._and_clauses))

    def _all_ors(self):
        temp_ors = ""
        if self._or_clauses:
            temp_ors = " or ".join(map(str, self._or_clauses))
            if self._and_clauses:
                temp_ors = "or " + temp_ors
        return temp_ors

