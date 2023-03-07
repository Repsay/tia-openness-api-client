from System import ICloneable, IFormatProvider

class CultureInfo(ICloneable, IFormatProvider):
    def __init__(self, *args, **kwargs) -> None:
        """Given a locale name, construct a CultureInfo object.

        Parameters:
            name: The name of the locale.
            useUserOverride: If true, to use the user-selected culture settings.

        Examples:
            >>> CultureInfo("en-US")
            >>> CultureInfo("en-US", True)

        """
        ...
