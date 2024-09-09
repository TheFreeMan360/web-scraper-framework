import abc


class ILoader(abc.ABC):

    @abc.abstractmethod
    def load(self) -> None:
        pass
