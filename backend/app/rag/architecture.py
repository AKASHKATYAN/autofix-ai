from dataclasses import dataclass, field


@dataclass
class Architecture:

    repository_name: str

    modules: list[str]

    architecture_summary: str = ""

    entry_points: list[str] = field(
        default_factory=list
    )

    core_modules: list[str] = field(
        default_factory=list
    )