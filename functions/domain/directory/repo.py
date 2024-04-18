from abc import ABC, abstractmethod

from .directory import Directory


class IDirectoryRepo(ABC):
    @abstractmethod
    def add(self, item: Directory): ...

    @abstractmethod
    def get(self, id: str) -> Directory: ...

    @abstractmethod
    def update(self, item: Directory): ...
