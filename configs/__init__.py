from .config import *

try:
    from .dev_config import *
except Exception:
    from .test_config import *

from .logging_config import *