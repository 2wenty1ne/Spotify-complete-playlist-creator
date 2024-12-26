from dataclasses import dataclass, field
from typing import List


@dataclass()
class Song:
    name: str
    song_uri: str
    album: str
    album_type: str = field(repr=False)
    tracknumber: int = field(repr=False)
    main_artist_id: str
    artist_ids: List[str]
