# Importing external modules to be reimported by project files

import datetime
import os

class Namespace():
    pass

external_modules=Namespace()
external_modules.datetime=datetime
external_modules.os=os