# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
# test.assert_equals(cakes(recipe, available), 2, 'Wrong result for example #1')


def cakes(recipe, available):
    max_make = None
    for var, val in recipe.iteritems():
        n = available.get(var, 0) // val
        if max_make is None or n < max_make:
            max_make = n
    return n
