import graphene


class Query(object):
    foo = graphene.String()
    def resolve_foo(self, info, **kwargs):
        return "Foo"


class Mutation(object):
    """
    Main mutations
    """
