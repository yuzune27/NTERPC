import dataclasses

@dataclasses.dataclass
class TimeStamps:
    start: int


@dataclasses.dataclass
class Assets:
    large_image: str
    large_text: str
    small_image: str
    small_text: str


@dataclasses.dataclass
class Buttons:
    label: str
    url: str


@dataclasses.dataclass
class RPCData:
    details: str
    state: str
    timestamps: TimeStamps
    assets: Assets
    buttons: list[Buttons]

def convert_to_dict(data: RPCData) -> dict:
    return dataclasses.asdict(data)