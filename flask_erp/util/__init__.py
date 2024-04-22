def json_to_entity(json_data, entity_class):
    """
    Maps JSON data to an instance of the specified entity class.

    Args:
    - json_data (dict): JSON data to be mapped.
    - entity_class (class): The class of the entity to be instantiated.

    Returns:
    - An instance of the entity class populated with data from the JSON.
    """
    instance = entity_class()
    for key, value in json_data.items():
        if hasattr(instance, key):
            setattr(instance, key, value)
    return instance
