# Program 3: Advanced Metaclass and Descriptor Protocol
# =====================================================

from typing import Any, Callable, Dict, List, Optional
import weakref

class ValidationDescriptor:
    """Program 3: Custom descriptor with validation logic"""
    def __init__(self, validate_funciton: Callable[[Any],bool], error_msg: str):
        self.validator = validate_funciton
        self.error_msg = error_msg
        self.data = weakref.WeakKeyDictionary
