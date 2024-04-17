from datetime import date
from typing import List, Optional
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class UserPrivilegeLevelOnDocument(Enum):
    READ_ONLY = "READ_ONLY"
    READ_AND_WRITE = "READ_AND_WRITE"


class UserWithAccessData(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    user_id: UUID = Field(alias="userId")
    privilege_level: UserPrivilegeLevelOnDocument = Field(alias="privilegeLevel")


class AuthorData(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    name: str = Field()
    surnames: List[str] = Field()


class BiblioGraphicInfo(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    authors: List[AuthorData] = Field()
    title: str = Field()
    publisher: str = Field()
    publishment_date: Optional[date] = Field(alias="publishmentDate")


class SummarySection(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    title: str = Field()
    body: str = Field()


class Summary(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    secctions: List[SummarySection] = Field()


class KeyConcept(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    id: UUID = Field()
    name: str = Field()
    description: str = Field()
    relationships: List[UUID] = Field()


class Relationship(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    father_concept_id: UUID = Field(alias="fatherConceptId")
    child_concept_id: UUID = Field(alias="childConceptId")
    description: str = Field()


class Document(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    id: str = Field()
    owner_id: str = Field(alias="ownerId")
    id_raw_doc: str = Field(alias="idRawDoc")
    name: str = Field(alias="name")
    extension: str = Field(alias="extension")
    parsed_llm_input: Optional[List[str]] = Field(alias="parsedLLMInput")
    users_with_access: List[UserWithAccessData] = Field(alias="usersWithAccess")
    bibliographic_info: Optional[BiblioGraphicInfo] = Field(
        None, alias="biblioGraficInfo"
    )
    summary: Optional[Summary] = None
    key_concepts: Optional[List[KeyConcept]] = Field(None, alias="keyConcepts")
    relationships: Optional[List[Relationship]] = None
