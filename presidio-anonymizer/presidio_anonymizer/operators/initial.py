"""Replaces the PII text entitiy with initials of the original name"""

from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Replaces the string with Initials"""
    def operate(self, text: str, params: Dict = None) -> str:
        """return the first letter of the name, followed by a period"""
        if not text:
            return ""
        name_s_ = text.split()
        initial = ""
        for word in name_s_:
            for char in word:
                if not (char.isalpha() or char.isnumeric()):
                    initial += char
                else:
                    if char.isalpha():
                        char = char.upper()
                    initial += char + ". "
                    break
        return initial.strip()
    
    def validate(self, params: Dict = None) -> None:
        """Initial does not require any parameters so no validation is needed"""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"
    
    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize
