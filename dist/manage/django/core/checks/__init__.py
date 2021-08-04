from .messages import (
    CRITICAL, DEBUG, ERROR, INFO, WARNING, CheckMessage, Critical, Debug,
    Error, Info, Warning,
)
from .registry import Tags, register, run_checks, tag_exists

# Import these to force registration of checks


__all__ = [
    'CheckMessage',
    'Debug', 'Info', 'Warning', 'Error', 'Critical',
    'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL',
    'register', 'run_checks', 'tag_exists', 'Tags',
]
