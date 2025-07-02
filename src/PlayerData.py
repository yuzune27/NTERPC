import dataclasses

@dataclasses.dataclass
class PlayerData:
    Player: str
    UID: int
    UIDVisible: bool
    BtnLabel: str
    BtnUrl: str