# -*- coding: utf-8 -*-
"""
"""
__authors__ = ["Karsten-Kai König <kkoenig@posteo.de>"]
__copyright__ = "Copyright (C) 2012 Karsten-Kai König <kkoenig@posteo.de>"
__license__ = """
keepassdb is free software: you can redistribute it and/or modify it under the terms
of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or at your option) any later version.

keepassdb is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
keepassdb.  If not, see <http://www.gnu.org/licenses/>.
"""

class KPError(Exception):
    """
    KPError is the base exception class to handle exception raised by keepassdb.
    """
class ReadOnlyDatabase(KPError):
    """
    Error when database was opened read-only.
    """
    pass

class InvalidDatabase(KPError):
    """
    Error raised when database appears to be invalid. :)
    """
    
class DatabaseAlreadyLocked(KPError):
    """
    Raised when the database is already locked.
    """
    
class UnsupportedDatabaseVersion(KPError):
    """
    Error raised when attempting to open a database version that is newer (e.g. KeePass2).
    """

class UnsupportedDatabaseEncryption(KPError):
    pass

class AuthenticationError(KPError):
    """
    Exception raised when contents cannot be verified against signature.
    """
    
class IncorrectKey(KPError):
    """
    Exception raised when contents cannot be decrypted with specified key.
    """
    
class ParseError(KPError):
    """
    Exception raised when unable to parse various database structures. 
    """
    