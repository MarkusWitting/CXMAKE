class FUNCDEF:
    def __init__(self, name, param_defs):
        self.name = name
        self.param_defs = param_defs

class FUNC:
    def __init__(self, name, params):
        self.name = name
        self.params = []
    
# Parameter  Declaration for functions
class PARAMDEF:
    def __init__(self, name, optional=False, default_value=None):
        self.name = name # Parameter name
        self.default_value = default_value # Default value assigned to parameter, if any
        self.optional = optional # Is parameter optional or required

class PARAM:
    def __init__(self, name, value=None):
        self.name = name # Parameter name
        self.value = value # Value assigned to parameter, if any

# Variable Declaration
class VARDCL:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value


PDEF = PARAMDEF
###=------ DEFINITIONS ------=###
FUNCS = [
    FUNCDEF("CXMAKE_Version",      [PDEF("Version")]),

    FUNCDEF("Project",             [PDEF("Name"), PDEF("Version", True), PDEF("Language")]),

    FUNCDEF("Build",               [PDEF("ReleaseMode")]),

    FUNCDEF("set",                 [PDEF("varname"), PDEF("value")]),

    FUNCDEF("dir"   ,              [PDEF("dir"), PDEF("RECURSIVE", True, "0"), PDEF("filetype", True, None)]),

    FUNCDEF("add_executable",      [PDEF("name"), PDEF("srcs")]),

    FUNCDEF("include_directories", [PDEF("dirs")]),

    FUNCDEF("add_subdirectory",    [PDEF("dir")]),
]
