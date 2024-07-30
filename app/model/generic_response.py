"""
    Generic Response Models

    This module contains the GenericResponse class for handling generic responses.

    Author
    ----------
    name: Ashfak Ahamed
    email: mzashfak@gmail.com

    Developers
    ----------
    - name: Ashfak Ahamed
    email: mzashfak@gmail.com

"""
from typing import Optional, Any


class GenericResponse:
    """
    GenericResponse Class

    This class is used to create generic responses with a success or failure status, a message, and results.

    Attributes:
    ----------
    is_error : bool
        The error status of the response
    message : str
        The message of the response
    results : Optional[Any]
        The results of the response, can be any type or None
    """
    def __init__(self, is_error: bool, message: str, results: Optional[Any]):  # results can be any type or None
        """
        Constructs a new instance of the GenericResponse class.

        Parameters:
        ----------
        is_error : bool
            The error status of the response
        message : str
            The message of the response
        results : Optional[Any]
            The results of the response, can be any type or None
        """
        self.is_error = is_error
        self.message = message
        self.results = results

    @classmethod
    def success(cls, message: str, results: Optional[Any]):
        """
          Creates a successful GenericResponse instance.

          Parameters:
          ----------
          message : str
              The message of the response
          results : Optional[Any]
              The results of the response, can be any type or None

          Returns:
          ----------
          GenericResponse
              A GenericResponse instance with is_error set to False
          """
        return cls(is_error=False, message=message, results=results)

    @classmethod
    def failed(cls, message: str, results: Optional[Any]):
        """
        Creates a failed GenericResponse instance.

        Parameters:
        ----------
        message : str
            The message of the response
        results : Optional[Any]
            The results of the response, can be any type or None

        Returns:
        ----------
        GenericResponse
            A GenericResponse instance with is_error set to True
        """
        return cls(is_error=True, message=message, results=results)
