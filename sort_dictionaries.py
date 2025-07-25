def sort_dictionaries(arr: list[dict], key, reverse=False) -> list[dict]:
    
    try:
        return sorted(
            arr,
            key=lambda x: x[key],
            reverse=False
        )
    except KeyError as e:
        print(f"Key \"{key}\" is not present in every dictionary !")
