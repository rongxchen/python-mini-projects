import uuid


def generate_id(prefix: str = "", remove_hyphens: bool = True):
    _id = str(uuid.uuid4())
    if remove_hyphens:
        _id = _id.replace("-", "")
    if prefix != "":
        _id = f"{prefix}-{_id}"
    return _id
