from pydantic import BaseModel


class Event(BaseModel):
    city: str
    venue: str
    date: str
    vibe: str


class SetHighlight(BaseModel):
    title: str
    bpm: str
    energy: str
    description: str


class SiteContent(BaseModel):
    stage_name: str
    tagline: str
    genres: list[str]
    events: list[Event]
    highlights: list[SetHighlight]
    contact_email: str
