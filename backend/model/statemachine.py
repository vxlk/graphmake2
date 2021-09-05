# The python reader state machine

class state():
    def __init__(self) -> None:
        pass

    def revert(self) -> state:
        pass

    def apply(self, next_state : state) -> state:
        pass

class state_machine():
    def __init__(self) -> None:
        self._state = state()

    def apply(self, next_state : state) -> state:
        return self._state.apply(next_state)

    def revert(self) -> state:
        return self._state.revert()

    def eval(self) -> None:
        pass