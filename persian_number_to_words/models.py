from dataclasses import dataclass
from typing import Optional


@dataclass
class NumberResult:
    formatted: str
    words: str
    language: str
    currency: Optional[str] = None

    def to_dict(self):
        return {
            "formatted": self.formatted,
            "words": self.words,
            "language": self.language,
            "currency": self.currency,
        }

    def __str__(self):
        return f"{self.formatted}\n{self.words}"
