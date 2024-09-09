import abc


class IDriver(abc.ABC):

    def __init__(self, **setings) -> None:
        super().__init__()

    @abc.abstractmethod
    def get(self, url: str) -> None: pass

    @abc.abstractmethod
    def close(self) -> None: pass

    @abc.abstractmethod
    def __enter__(self) -> "IDriver": pass
    # return self

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: pass
    # self.close()
