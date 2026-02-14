from app.services.errors import (UniqueContraintError,
                                 DeactivatedResourceError)


def check_id(obj_name, id, repo):
    """
    Docstring pour check_id

    :param obj_name: Is the name of the object id checked
    :param id: Is the id of the object
    :param repo: Is an instance of the object repository

    This function check if the id refer to an existing object
    in database.
    """
    obj = repo.get_id(id)
    if not obj:
        raise LookupError(
            f'{obj_name} {id} not found')
    if obj.is_active is False:
        raise DeactivatedResourceError(
            f'{obj_name} {id} exist but is deactivated')
    else:
        return obj


def check_unique(obj_name, key, value, repo):
    """
    Docstring pour check_unique

    :param obj_name: The entity name
    :param key: The key/attribute name of the entity
    :param value: The expected value for the key/attribute of the entity
    :param repo: Is an instance of the object repository
    """
    obj = repo.get_by_attribute(key, value)
    if len(obj) != 0 and obj[0].is_active is True:
        raise UniqueContraintError(f'{obj_name} already exists')
    if len(obj) != 0 and obj.is_active is False:
        raise UniqueContraintError(
            f'Deactivated {obj_name} exist with this {key}')
