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
    def __init__(self, name, index, optional=False, default_value=None):
        self.name = name # Parameter name
        self.index = index # What number parameter it is in potential list of parameters
        self.default_value = default_value # Default value assigned to parameter, if any
        self.optional = optional # Is parameter optional or required

class PARAM:
    def __init__(self, name, index, value=None):
        self.name = name # Parameter name
        self.index = index # What number parameter it is in potential list of parameters
        self.value = value # Value assigned to parameter, if any

# Variable Declaration
class VARDCL:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

<<<<<<< Updated upstream
class FLAGDEF:
    def __init__(self, name, description=None):
        self.name = name
        self.description = description


=======



>>>>>>> Stashed changes
PDEF = PARAMDEF
###=------ DEFINITIONS ------=###
FUNCS = [
    FUNCDEF("CXMAKE_Version",      [PDEF("Version", 0)]),

    FUNCDEF("Project",             [PDEF("Name", 0), PDEF("Version", 1, True), PDEF("Language", 2)]),

    FUNCDEF("Build",               [PDEF("ReleaseMode", 0)]),

    FUNCDEF("set",                 [PDEF("varname", 0), PDEF("value", 1)]),

    FUNCDEF("dir"   ,              [PDEF("dir", 0), PDEF("RECURSIVE", 0, True, "0"), PDEF("filetype", 1, True, None)]),
<<<<<<< Updated upstream

    FUNCDEF("add_executable",      [PDEF("name", 0), PDEF("srcs", 1)]),

=======

    FUNCDEF("add_executable",      [PDEF("name", 0), PDEF("srcs", 1)]),

>>>>>>> Stashed changes
    FUNCDEF("include_directories", [PDEF("dirs", 0)]),

    FUNCDEF("add_subdirectory",    [PDEF("dir", 0)]),
]
<<<<<<< Updated upstream

FLAGS = [

]
=======
>>>>>>> Stashed changes
