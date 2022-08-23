import datetime

from book import Book
from recipe import Recipe

bolognaise = Recipe("bolognaise", 4, 30, ["viande", "oignons", "celeri", "carottes", "tomates"], "sauce a la viande", "lunch")

dico_test = {
    "lunch": bolognaise
}

italian = Book("Italian recipes", datetime.date.today(), datetime.date.today(), dico_test)
print(bolognaise)
print(italian)

