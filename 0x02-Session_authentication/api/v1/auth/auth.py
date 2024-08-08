#!/usr/bin/env python3
"""Auth class"""
from typing import List, TypeVar
from flask import request
from os import getenv


class Auth:
    """Auth class to manage API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Public method to check if authentication is required for a given path.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): The list of paths that
            do not require authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if not path or not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        for ex_path in excluded_paths:
            if not ex_path.endswith('/'):
                ex_path += '/'
            if path == ex_path or path.startswith(ex_path.split('*')[0]):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Public method to get the authorization header from the request.

        Args:
            request: The request object.

        Returns:
            str: The authorization header if present, None otherwise.
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Public method to get the current user from the request.

        Args:
            request: The request object.

        Returns:
            TypeVar('User'): The current user, None by default.
        """
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request:"""
        if not request:
            return None
        _my_session_id = getenv('SESSION_NAME')
        return request.cookies.get(_my_session_id)
