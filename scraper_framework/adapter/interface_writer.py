import abc


class IWriter(abc.ABC):

    @abc.abstractmethod
    def write(self) -> None:
        pass
