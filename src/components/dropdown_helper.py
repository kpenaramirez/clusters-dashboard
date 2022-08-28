def to_dropdown_options(values: list[str]) -> list[dict[str, str]]:
    """Code frequently used in the dropdowns menu to list the options"""
    return [{"label": value.replace("_", " "), "value": value} for value in values]