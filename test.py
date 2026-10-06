def has_internal_copyright(content: str, entities: list[str] | None = None) -> bool:
    """
    Check whether content contains a copyright line naming an internal entity.

    Args:
        content: Diff content for a single file change.
        entities: Copyright-holder substrings to match; defaults to
            DEFAULT_INTERNAL_ENTITIES.

    Returns:
        True if any copyright-bearing line contains one of the entity strings.
    """
    if not isinstance(content, str):
        return False
    if entities is None:
        entities = DEFAULT_INTERNAL_ENTITIES

    copyright_lines = re.findall(_ADDED_COPYRIGHT_PATTERN, content, re.MULTILINE) + re.findall(
        _DELETED_COPYRIGHT_PATTERN, content, re.MULTILINE
    )
    return any(entity in line for line in copyright_lines for entity in entities)
