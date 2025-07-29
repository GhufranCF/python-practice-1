def sort_dictionaries(arr: list[dict], key, reverse=False) -> list[dict]:
    return sorted(
        arr,
        key=lambda x: x[key],
        reverse=False
    )
