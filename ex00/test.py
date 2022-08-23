from book import Book
from recipe import Recipe

bolognaise = Recipe("bolognaise", 4, 30, ["viande", "oignons", "celeri", "carottes", "tomates"], "sauce a la viande", "lunch")


to_print = str(bolognaise)
print(to_print)

