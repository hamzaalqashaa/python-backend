def merge_with_conflict_handling(dict1: dict, dict2: dict) -> dict:
    """
    Merge two dictionaries and handle key conflicts using the walrus operator.

    If a key is in both dicts, the value from dict2 is used,
    and a message is printed showing the conflict.

    Args:
        dict1 (dict): First dictionary.
        dict2 (dict): Second dictionary.

    Returns:
        dict: The merged dictionary.
    """
    merged = dict1.copy()

    for key, value in dict2.items():
        if (existing := merged.get(key)) is not None:
            print(f"Conflict for key '{key}': dict1 has {existing}, dict2 has {value}")
        merged[key] = value  # Use value from dict2 regardless

    return merged


if __name__ == "__main__":
    dict1 = {"name": "Alice", "age": 25, "city": "Amman"}
    dict2 = {"age": 30, "country": "Jordan", "city": "Irbid"}

    result = merge_with_conflict_handling(dict1, dict2)
    print("\nMerged dictionary:", result)
