def split_book_id(book_id: str) -> tuple[str, str] | None:
    parts = book_id.split(":")
    if len(parts) != 2 or not all(parts):
        return None
    return parts[0], parts[1]