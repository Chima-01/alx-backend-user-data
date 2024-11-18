#!/usr/bin/env python3
"""
 Implement a basic Auth
"""
from flask import Flask
from typing import List, TypeVar


class Auth:
    """ class auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ return False
        """
        if not path or not excluded_paths:
            return True
        if not path.endswith("/"):
            path = path + "/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ returns None
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ return None
        """
        return None
