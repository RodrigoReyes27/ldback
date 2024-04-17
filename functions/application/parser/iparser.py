from typing import Any
from typing import Tuple
from io import BytesIO
from abc import ABC, abstractmethod

from pydantic import BaseModel, ConfigDict, Field


class DocumentImage(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: str = Field()
    data: Any = Field()


class ParsingResult(BaseModel):
    model_config = ConfigDict(frozen=True)

    text: str = Field()
    images: Tuple["DocumentImage"] = Field()


class IParser(ABC):
    """Takes a file determined by the implementation of the interface and
    returns an object of type Parsing Result
    """

    @abstractmethod
    def parse(self, file: BytesIO) -> ParsingResult: ...
