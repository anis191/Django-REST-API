from django.core.exceptions import ValidationError

def validate_file_size(file):
    """This validator validate if file size is less then 10 MB"""
    max_size = 10
    max_size_in_bytes = max_size * 1024 * 1024

    if file.size > max_size_in_bytes:
        raise ValidationError(f"File can't be larger then {max_size}MB!")

"""
Here file(image..) means those fields where we add a validator.
"""