from abc import ABC, abstractmethod
from typing import List
from pydantic import BaseModel, ConfigDict, Field

from .document import BiblioGraphicInfo, Summary


class TextInsight(BaseModel):
    model_config = ConfigDict(frozen=True)

    bibliografic_info: BiblioGraphicInfo = Field()
    key_concepts: List[str] = Field()
    summary: Summary = Field()


class ITextInsightExtractor(ABC):

    @abstractmethod
    def extract_insight(self, text_body: str) -> TextInsight: ...
