from fastapi import APIRouter

from app.models import Event, SetHighlight, SiteContent

router = APIRouter(prefix="/api", tags=["kaywe"])


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/content", response_model=SiteContent)
def get_content() -> SiteContent:
    return SiteContent(
        stage_name="DJ KAYWE",
        tagline="Liquid beats. Glassy visuals. Pure club energy.",
        genres=["Afro House", "Melodic Techno", "Future Bass", "Amapiano"],
        events=[
            Event(city="Berlin", venue="Nocturne Hall", date="2026-03-14", vibe="Neon Pulse"),
            Event(city="Hamburg", venue="Dockyard Club", date="2026-04-04", vibe="Sunrise Set"),
            Event(city="Cologne", venue="Skyline 9", date="2026-05-01", vibe="Deep Liquid"),
        ],
        highlights=[
            SetHighlight(
                title="Midnight Flow",
                bpm="124 BPM",
                energy="Hypnotic",
                description="Layered percussion and atmospheric synth textures for late-night sessions.",
            ),
            SetHighlight(
                title="Aurora Rise",
                bpm="128 BPM",
                energy="Uplifting",
                description="Emotional builds and melodic drops that peak right before sunrise.",
            ),
            SetHighlight(
                title="Bass Mirage",
                bpm="130 BPM",
                energy="Explosive",
                description="Heavy bass movement blended with clean vocal chops and tight transitions.",
            ),
        ],
        contact_email="booking@kaywe.dj",
    )
