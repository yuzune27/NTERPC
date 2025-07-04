from dataclasses import dataclass, asdict


@dataclass
class TimeStamps:
    start: int


@dataclass
class Assets:
    large_image: str
    large_text: str
    small_image: str
    small_text: str


@dataclass
class RPCData:
    details: str
    state: str
    timestamps: TimeStamps
    assets: Assets


def convert_to_dict(data: RPCData) -> dict:
    return asdict(data)
