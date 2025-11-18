"""Replaces the PII text entitiy with initials of the original name"""

from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Replaces the string with Initials"""
    def operate(self, text: str = None, params: Dict = None) -> str:
        """return the first letter of the name, followed by a period"""
        if not text:
            return ""
        return f"{text[0]}."
    
    def validate(self, params: Dict = None) -> None:
        """Initial does not require any parameters so no validation is needed"""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"
    
    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize
