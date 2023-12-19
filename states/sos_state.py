class SosState(StatesGroup):
    """
    Represents the states for managing SOS (emergency) interactions.
    """
    question = State()
    """
    State for asking a question during an SOS interaction
    """
    submit = State()
    """
    State for submitting an SOS request
    """

class AnswerState(StatesGroup):
    """
    Represents the states for managing answers to SOS requests.
    """
    answer = State()
    """
    State for providing an answer to an SOS request
    """
    submit = State()
    """
    State for submitting the answer to an SOS request
    """