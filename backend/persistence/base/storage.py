from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def read(self) -> dict:
        pass

    @abstractmethod
    def write(self, data: dict) -> None:
        pass

    @abstractmethod
    def exists(self) -> bool:
        pass

    @abstractmethod
    def read_list(self, key: str) -> list:
        pass

    @abstractmethod
    def write_list(self, key: str, values: list) -> None:
        pass