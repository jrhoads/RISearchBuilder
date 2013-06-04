from riSearchBuilder import RISearchBuilder, RITriple

ri = RISearchBuilder()
ri.and_clause("$item <fedora-rels-ext:%s> <info:fedora/%s>" % ("isMemberOf", "bdr:2559"))
ri.and_clause("$item <bul-rel:hasPagination> $page" ). \
        order_by("$page")
print ri.serialize(joiner=' ')


ri2 = RISearchBuilder()
ri2.and_clause( RITriple("$item", "<fedora-rels-ext:%s>" % "isAnnotationOf", "<info:fedora/%s>" % "bdr:11111"))
ri2.and_clause("$item <bul-rel:hasPagination> $page" ). \
        order_by("$monkey")
print ri2.serialize("\n")
