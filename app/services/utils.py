from app.services.errors import (UniqueContraintError,
                                 DeactivatedResourceError)


def check_id(obj_name, id, repo):
    """
    Checks if the id refer to an existing object
    in database.

    :param obj_name: Name of the object to return it in error msg
    :param id: Id of the object
    :param repo: Instance of the object repository
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
    Checks a unique constrainted field by looking for
    another entity already existing with this value for this
    unique constrainted field.

    :param obj_name: The entity name
    :param key: The key/attribute name of the entity
    :param value: The expected value for the key/attribute of the entity
    :param repo: Is an instance of the object repository
    """
    obj = repo.get_by_attribute(key, value)
    if len(obj) != 0 and obj[0].is_active is True:
        raise UniqueContraintError(f'{obj_name} already exists')
    if len(obj) != 0 and obj[0].is_active is False:
        raise UniqueContraintError(
            f'Deactivated {obj_name} exist with this {key}')
