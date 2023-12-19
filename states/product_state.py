from aiogram.dispatcher.filters.state import StatesGroup, State

class ProductState(StatesGroup):
    """
    Represents the states for managing product information.
    """
    title = State()
    """
         State for entering the product title
    """
    body = State()
    """
        State for entering the product description
    """
    image = State()
    """
        State for selecting/uploading the product image
    """
    price = State()
    """
        State for entering the product price
    """
    confirm = State()
    """
        State for confirming the product details
    """

class CategoryState(StatesGroup):
    """
    Represents the states for managing category information.
    """
    title = State()
    """
    State for entering the category title
    """