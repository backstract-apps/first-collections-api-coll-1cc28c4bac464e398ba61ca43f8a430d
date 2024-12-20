from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class BUser(BaseModel):
    id: int
    created_at: datetime.time


class ReadBUser(BaseModel):
    id: int
    created_at: datetime.time
    class Config:
        from_attributes = True


