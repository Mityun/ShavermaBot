from aiogram.dispatcher.filters.state import StatesGroup, State

class CheckoutState(StatesGroup):
    """
    Represents the states for the checkout process.
    """
    check_cart = State()
    """
       State for checking the cart
       """
    name = State()
    """
        State for entering the name
        """
    address = State()
    """
        State for entering the address
        """
    confirm = State()
    """
        State for confirming the order
        """