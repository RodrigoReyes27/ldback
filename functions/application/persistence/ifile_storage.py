from abc import ABC, abstractmethod
from typing import Tuple

from io import BytesIO
from enum import Enum


class FileMimeType(Enum):
    # conventionally text documents
    PDF = "application/pdf"
    PPT = "application/vnd.ms-powerpoint"
    PPTX = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    DOC = "application/msword"
    DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

    # conventionally image documents
    PNG = "image/png"
    WEBP = "image/webp"
    JPEG = "image/jpeg"


mimetypes_to_extensions = {
    FileMimeType.PDF: ".pdf",
    FileMimeType.PPT: ".ppt",
    FileMimeType.PPTX: ".pptx",
    FileMimeType.DOC: ".doc",
    FileMimeType.DOCX: ".docx",
    FileMimeType.PNG: ".png",
    FileMimeType.WEBP: ".webp",
    FileMimeType.JPEG: ".jpeg",
}


class IFileStorage(ABC):
    @abstractmethod
    def add(self, file: BytesIO, mimetype: FileMimeType) -> str:
        """Returns url pointing to the file in the storage bucket to access it with a library
        from the provider of the concrete class wether it is GoogleCloud, AWS or Azure
        """

    @abstractmethod
    def get(self, file_url: str) -> Tuple[BytesIO, FileMimeType]:
        """Returns BytesIO of the file identified by file_url"""

    @abstractmethod
    def delete(self, file_url: str):
        """Deletes the file identified by file_url"""
