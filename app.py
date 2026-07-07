from typing import Literal

MaritalStatus = Literal["single", "married", "divorced", "widowed"]


def is_legal_age(age: int, marital_status: MaritalStatus) -> bool:
    """Determine whether a person is of legal age under Thai law.

    In Thailand, the general age of majority is 20 years old. A person who is
    under 20 may still be treated as an adult for legal purposes if they are
    married or divorced.
    """
    if age >= 20:
        return True

    if marital_status in {"married", "divorced"}:
        return True

    return False
