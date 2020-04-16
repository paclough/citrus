from .source_resource_test import *
from .exceptions_test import *
from .scenarios_test import *
from .maps_test import *
from .organiztions_test import *
from .harvest_test import *
from .transform_test import *

import configparser
from pathlib import Path
import sys


# Locating configs
if os.getenv('CITRUS_CONFIG'):
    CONFIG_PATH = Path(os.getenv('CITRUS_CONFIG'))
elif os.path.exists(os.path.join(Path.home(), '.local/share/citrus/citrus.cfg')):
    CONFIG_PATH = os.path.join(Path.home(), '.local/share/citrus')
elif os.path.exists(os.path.join(Path(__file__).parents[0], 'citrus.cfg')):
    CONFIG_PATH = Path(__file__).parents[0]
else:
    print("Cannot locate citrus configs.")  # TODO: This can return a more helpful prompt, or build default configs
    sys.exit(1)

citrus_config = configparser.ConfigParser()
citrus_config.read(os.path.join(CONFIG_PATH, 'citrus.cfg'))
custom_map_test_path = citrus_config['ssdn']['CustomMapPath']

try:
    sys.path.append(custom_map_test_path)
    from custom_map_tests import *
except ModuleNotFoundError:
    pass
