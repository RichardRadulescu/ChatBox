from typing import Optional

from pydantic import BaseModel, ConfigDict, model_validator


class FileWrite(BaseModel):
    name: str
    type: str
    text_content: Optional[str] = None
    blob_content: Optional[bytes] = None

    @model_validator(mode="after")
    def check_content_exists(self) -> "FileWrite":
        if not self.text_content and not self.blob_content:
            raise ValueError("File must have content")
        return self


class FileRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    type: str
    text_content: Optional[str] = None
    blob_content: Optional[bytes] = None

    @model_validator(mode="after")
    def check_content_exists(self) -> "FileRead":
        if not self.text_content and not self.blob_content:
            raise ValueError("File must have content")
        return self
