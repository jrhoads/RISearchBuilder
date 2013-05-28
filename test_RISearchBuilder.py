from RISearchBuilder import RISearchBuilder

ri = RISearchBuilder()
ri.and_clause("$item <fedora-rels-ext:%s> <info:fedora/%s>" % ("isMemberOf", "bdr:2559"))
ri.and_clause("$item <bul-rel:hasPagination> $page" )
ri.and_clause("$sub $pred $obj"). \
        and_clause("$sub $bpred MOO"). \
        or_clause("$may $or $sub")
print ri.serialize(joiner=' ')
