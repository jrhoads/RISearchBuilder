from riSearchBuilder import RISearchBuilder

ri = RISearchBuilder()
ri.and_clause("$item <fedora-rels-ext:%s> <info:fedora/%s>" % ("isMemberOf", "bdr:2559"))
ri.and_clause("$item <bul-rel:hasPagination> $page" ). \
        order_by("$page")
print ri.serialize(joiner=' ')
