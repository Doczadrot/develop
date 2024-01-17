def to_uppercase(input_str):
    """
    Converts the input string to uppercase.

    Parameters:
    input_str (str): The input string.

    Returns:
    str: The uppercase string.
    """
    return input_str.upper()

def capitalize_first_letters(input_str):
    """
    Capitalizes the first letter of each word in the input string.

    Parameters:
    input_str (str): The input string.

    Returns:
    str: The string with first letters of each word capitalized.
    """
    words = input_str.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
