
# Code By : ALIF FUSOBAR - master@itsecurity.id - www.itsecurity.id

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pytrch', [dirname(__file__)])
        except ImportError:
            import _pytrch
            return _pytrch
        if fp is not None:
            try:
                _mod = imp.load_module('_pytrch', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pytrch = swig_import_helper()
    del swig_import_helper
else:
    import _pytrch
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


from _pytrch import TrchError as TrchError


def Exc_Trch(*args):
  return _pytrch.Exc_Trch(*args)
Exc_Trch = _pytrch.Exc_Trch

def Parameter_Boolean_getValue(*args):
  return _pytrch.Parameter_Boolean_getValue(*args)
Parameter_Boolean_getValue = _pytrch.Parameter_Boolean_getValue

def Parameter_IPv4_getValue(*args):
  return _pytrch.Parameter_IPv4_getValue(*args)
Parameter_IPv4_getValue = _pytrch.Parameter_IPv4_getValue

def Parameter_IPv6_getValue(*args):
  return _pytrch.Parameter_IPv6_getValue(*args)
Parameter_IPv6_getValue = _pytrch.Parameter_IPv6_getValue

def Parameter_LocalFile_getValue(*args):
  return _pytrch.Parameter_LocalFile_getValue(*args)
Parameter_LocalFile_getValue = _pytrch.Parameter_LocalFile_getValue

def Parameter_Port_getValue(*args):
  return _pytrch.Parameter_Port_getValue(*args)
Parameter_Port_getValue = _pytrch.Parameter_Port_getValue

def Parameter_S8_getValue(*args):
  return _pytrch.Parameter_S8_getValue(*args)
Parameter_S8_getValue = _pytrch.Parameter_S8_getValue

def Parameter_S16_getValue(*args):
  return _pytrch.Parameter_S16_getValue(*args)
Parameter_S16_getValue = _pytrch.Parameter_S16_getValue

def Parameter_S32_getValue(*args):
  return _pytrch.Parameter_S32_getValue(*args)
Parameter_S32_getValue = _pytrch.Parameter_S32_getValue

def Parameter_S64_getValue(*args):
  return _pytrch.Parameter_S64_getValue(*args)
Parameter_S64_getValue = _pytrch.Parameter_S64_getValue

def Parameter_U8_getValue(*args):
  return _pytrch.Parameter_U8_getValue(*args)
Parameter_U8_getValue = _pytrch.Parameter_U8_getValue

def Parameter_U16_getValue(*args):
  return _pytrch.Parameter_U16_getValue(*args)
Parameter_U16_getValue = _pytrch.Parameter_U16_getValue

def Parameter_U32_getValue(*args):
  return _pytrch.Parameter_U32_getValue(*args)
Parameter_U32_getValue = _pytrch.Parameter_U32_getValue

def Parameter_U64_getValue(*args):
  return _pytrch.Parameter_U64_getValue(*args)
Parameter_U64_getValue = _pytrch.Parameter_U64_getValue

def Parameter_Socket_getValue(*args):
  return _pytrch.Parameter_Socket_getValue(*args)
Parameter_Socket_getValue = _pytrch.Parameter_Socket_getValue

def Parameter_String_getValue(*args):
  return _pytrch.Parameter_String_getValue(*args)
Parameter_String_getValue = _pytrch.Parameter_String_getValue

def Parameter_UString_getValue(*args):
  return _pytrch.Parameter_UString_getValue(*args)
Parameter_UString_getValue = _pytrch.Parameter_UString_getValue

def Parameter_Buffer_getValue(*args):
  return _pytrch.Parameter_Buffer_getValue(*args)
Parameter_Buffer_getValue = _pytrch.Parameter_Buffer_getValue

def Paramchoice_getValue(*args):
  return _pytrch.Paramchoice_getValue(*args)
Paramchoice_getValue = _pytrch.Paramchoice_getValue

def Config_create(*args):
  return _pytrch.Config_create(*args)
Config_create = _pytrch.Config_create

def Config_delete(*args):
  return _pytrch.Config_delete(*args)
Config_delete = _pytrch.Config_delete

def Config_duplicate(*args):
  return _pytrch.Config_duplicate(*args)
Config_duplicate = _pytrch.Config_duplicate

def Config_getConfigVersion(*args):
  return _pytrch.Config_getConfigVersion(*args)
Config_getConfigVersion = _pytrch.Config_getConfigVersion

def Config_getConstants(*args):
  return _pytrch.Config_getConstants(*args)
Config_getConstants = _pytrch.Config_getConstants

def Config_getID(*args):
  return _pytrch.Config_getID(*args)
Config_getID = _pytrch.Config_getID

def Config_getInputParams(*args):
  return _pytrch.Config_getInputParams(*args)
Config_getInputParams = _pytrch.Config_getInputParams

def Config_getName(*args):
  return _pytrch.Config_getName(*args)
Config_getName = _pytrch.Config_getName

def Config_getNamespaceUri(*args):
  return _pytrch.Config_getNamespaceUri(*args)
Config_getNamespaceUri = _pytrch.Config_getNamespaceUri

def Config_getOutputParams(*args):
  return _pytrch.Config_getOutputParams(*args)
Config_getOutputParams = _pytrch.Config_getOutputParams

def Config_getSchemaVersion(*args):
  return _pytrch.Config_getSchemaVersion(*args)
Config_getSchemaVersion = _pytrch.Config_getSchemaVersion

def Config_getVersion(*args):
  return _pytrch.Config_getVersion(*args)
Config_getVersion = _pytrch.Config_getVersion

def Config_marshal(*args):
  return _pytrch.Config_marshal(*args)
Config_marshal = _pytrch.Config_marshal

def Config_printUsage(*args):
  return _pytrch.Config_printUsage(*args)
Config_printUsage = _pytrch.Config_printUsage

def Config_setConstants(*args):
  return _pytrch.Config_setConstants(*args)
Config_setConstants = _pytrch.Config_setConstants

def Config_setInputParams(*args):
  return _pytrch.Config_setInputParams(*args)
Config_setInputParams = _pytrch.Config_setInputParams

def Config_setOutputParams(*args):
  return _pytrch.Config_setOutputParams(*args)
Config_setOutputParams = _pytrch.Config_setOutputParams

def Config_unmarshal(*args):
  return _pytrch.Config_unmarshal(*args)
Config_unmarshal = _pytrch.Config_unmarshal

def FinalizeXMLUnmarshal():
  return _pytrch.FinalizeXMLUnmarshal()
FinalizeXMLUnmarshal = _pytrch.FinalizeXMLUnmarshal

def InitializeXMLUnmarshal():
  return _pytrch.InitializeXMLUnmarshal()
InitializeXMLUnmarshal = _pytrch.InitializeXMLUnmarshal

def Params_addParamchoice(*args):
  return _pytrch.Params_addParamchoice(*args)
Params_addParamchoice = _pytrch.Params_addParamchoice

def Params_addParameter(*args):
  return _pytrch.Params_addParameter(*args)
Params_addParameter = _pytrch.Params_addParameter

def Params_create(*args):
  return _pytrch.Params_create(*args)
Params_create = _pytrch.Params_create

def Params_delete(*args):
  return _pytrch.Params_delete(*args)
Params_delete = _pytrch.Params_delete

def Params_duplicate(*args):
  return _pytrch.Params_duplicate(*args)
Params_duplicate = _pytrch.Params_duplicate

def Params_findParamchoice(*args):
  return _pytrch.Params_findParamchoice(*args)
Params_findParamchoice = _pytrch.Params_findParamchoice

def Params_findParameter(*args):
  return _pytrch.Params_findParameter(*args)
Params_findParameter = _pytrch.Params_findParameter

def Params_getName(*args):
  return _pytrch.Params_getName(*args)
Params_getName = _pytrch.Params_getName

def Params_getNumParamchoices(*args):
  return _pytrch.Params_getNumParamchoices(*args)
Params_getNumParamchoices = _pytrch.Params_getNumParamchoices

def Params_getNumParameters(*args):
  return _pytrch.Params_getNumParameters(*args)
Params_getNumParameters = _pytrch.Params_getNumParameters

def Params_getParamchoice(*args):
  return _pytrch.Params_getParamchoice(*args)
Params_getParamchoice = _pytrch.Params_getParamchoice

def Params_getParameter(*args):
  return _pytrch.Params_getParameter(*args)
Params_getParameter = _pytrch.Params_getParameter

def Params_isValid(*args):
  return _pytrch.Params_isValid(*args)
Params_isValid = _pytrch.Params_isValid

def Params_parseCommandLine(*args):
  return _pytrch.Params_parseCommandLine(*args)
Params_parseCommandLine = _pytrch.Params_parseCommandLine

def Params_printInvalid(*args):
  return _pytrch.Params_printInvalid(*args)
Params_printInvalid = _pytrch.Params_printInvalid

def Params_removeParameter(*args):
  return _pytrch.Params_removeParameter(*args)
Params_removeParameter = _pytrch.Params_removeParameter

def Params_getCallbackIPv4Values(*args):
  return _pytrch.Params_getCallbackIPv4Values(*args)
Params_getCallbackIPv4Values = _pytrch.Params_getCallbackIPv4Values

def Params_getCallbackIPv6Values(*args):
  return _pytrch.Params_getCallbackIPv6Values(*args)
Params_getCallbackIPv6Values = _pytrch.Params_getCallbackIPv6Values

def Params_getCallbackPortValues(*args):
  return _pytrch.Params_getCallbackPortValues(*args)
Params_getCallbackPortValues = _pytrch.Params_getCallbackPortValues

def Params_validateCallbackPorts(*args):
  return _pytrch.Params_validateCallbackPorts(*args)
Params_validateCallbackPorts = _pytrch.Params_validateCallbackPorts

def Paramchoice_addParamgroup(*args):
  return _pytrch.Paramchoice_addParamgroup(*args)
Paramchoice_addParamgroup = _pytrch.Paramchoice_addParamgroup

def Paramchoice_create(*args):
  return _pytrch.Paramchoice_create(*args)
Paramchoice_create = _pytrch.Paramchoice_create

def Paramchoice_delete(*args):
  return _pytrch.Paramchoice_delete(*args)
Paramchoice_delete = _pytrch.Paramchoice_delete

def Paramchoice_getDefaultValue(*args):
  return _pytrch.Paramchoice_getDefaultValue(*args)
Paramchoice_getDefaultValue = _pytrch.Paramchoice_getDefaultValue

def Paramchoice_getDescription(*args):
  return _pytrch.Paramchoice_getDescription(*args)
Paramchoice_getDescription = _pytrch.Paramchoice_getDescription

def Paramchoice_getName(*args):
  return _pytrch.Paramchoice_getName(*args)
Paramchoice_getName = _pytrch.Paramchoice_getName

def Paramchoice_getNumParamgroups(*args):
  return _pytrch.Paramchoice_getNumParamgroups(*args)
Paramchoice_getNumParamgroups = _pytrch.Paramchoice_getNumParamgroups

def Paramchoice_getParamgroup(*args):
  return _pytrch.Paramchoice_getParamgroup(*args)
Paramchoice_getParamgroup = _pytrch.Paramchoice_getParamgroup

def Paramchoice_hasValidValue(*args):
  return _pytrch.Paramchoice_hasValidValue(*args)
Paramchoice_hasValidValue = _pytrch.Paramchoice_hasValidValue

def Paramchoice_hasValue(*args):
  return _pytrch.Paramchoice_hasValue(*args)
Paramchoice_hasValue = _pytrch.Paramchoice_hasValue

def Paramchoice_isValid(*args):
  return _pytrch.Paramchoice_isValid(*args)
Paramchoice_isValid = _pytrch.Paramchoice_isValid

def Paramchoice_matchName(*args):
  return _pytrch.Paramchoice_matchName(*args)
Paramchoice_matchName = _pytrch.Paramchoice_matchName

def Paramchoice_setValue(*args):
  return _pytrch.Paramchoice_setValue(*args)
Paramchoice_setValue = _pytrch.Paramchoice_setValue

def Parameter_delete(*args):
  return _pytrch.Parameter_delete(*args)
Parameter_delete = _pytrch.Parameter_delete

def Parameter_getDescription(*args):
  return _pytrch.Parameter_getDescription(*args)
Parameter_getDescription = _pytrch.Parameter_getDescription

def Parameter_getFormat(*args):
  return _pytrch.Parameter_getFormat(*args)
Parameter_getFormat = _pytrch.Parameter_getFormat

def Parameter_getInvalidReason(*args):
  return _pytrch.Parameter_getInvalidReason(*args)
Parameter_getInvalidReason = _pytrch.Parameter_getInvalidReason

def Parameter_getMarshalledDefault(*args):
  return _pytrch.Parameter_getMarshalledDefault(*args)
Parameter_getMarshalledDefault = _pytrch.Parameter_getMarshalledDefault

def Parameter_getMarshalledValue(*args):
  return _pytrch.Parameter_getMarshalledValue(*args)
Parameter_getMarshalledValue = _pytrch.Parameter_getMarshalledValue

def Parameter_getName(*args):
  return _pytrch.Parameter_getName(*args)
Parameter_getName = _pytrch.Parameter_getName

def Parameter_getType(*args):
  return _pytrch.Parameter_getType(*args)
Parameter_getType = _pytrch.Parameter_getType

def Parameter_hasValue(*args):
  return _pytrch.Parameter_hasValue(*args)
Parameter_hasValue = _pytrch.Parameter_hasValue

def Parameter_hasValidValue(*args):
  return _pytrch.Parameter_hasValidValue(*args)
Parameter_hasValidValue = _pytrch.Parameter_hasValidValue

def Parameter_hide(*args):
  return _pytrch.Parameter_hide(*args)
Parameter_hide = _pytrch.Parameter_hide

def Parameter_isHidden(*args):
  return _pytrch.Parameter_isHidden(*args)
Parameter_isHidden = _pytrch.Parameter_isHidden

def Parameter_isRequired(*args):
  return _pytrch.Parameter_isRequired(*args)
Parameter_isRequired = _pytrch.Parameter_isRequired

def Parameter_isValid(*args):
  return _pytrch.Parameter_isValid(*args)
Parameter_isValid = _pytrch.Parameter_isValid

def Parameter_markInvalid(*args):
  return _pytrch.Parameter_markInvalid(*args)
Parameter_markInvalid = _pytrch.Parameter_markInvalid

def Parameter_markInvalidWithReason(*args):
  return _pytrch.Parameter_markInvalidWithReason(*args)
Parameter_markInvalidWithReason = _pytrch.Parameter_markInvalidWithReason

def Parameter_matchFormat(*args):
  return _pytrch.Parameter_matchFormat(*args)
Parameter_matchFormat = _pytrch.Parameter_matchFormat

def Parameter_matchFormatAndType(*args):
  return _pytrch.Parameter_matchFormatAndType(*args)
Parameter_matchFormatAndType = _pytrch.Parameter_matchFormatAndType

def Parameter_matchName(*args):
  return _pytrch.Parameter_matchName(*args)
Parameter_matchName = _pytrch.Parameter_matchName

def Parameter_matchType(*args):
  return _pytrch.Parameter_matchType(*args)
Parameter_matchType = _pytrch.Parameter_matchType

def Parameter_resetValue(*args):
  return _pytrch.Parameter_resetValue(*args)
Parameter_resetValue = _pytrch.Parameter_resetValue

def Parameter_setMarshalledValue(*args):
  return _pytrch.Parameter_setMarshalledValue(*args)
Parameter_setMarshalledValue = _pytrch.Parameter_setMarshalledValue

def Parameter_Boolean_create(*args):
  return _pytrch.Parameter_Boolean_create(*args)
Parameter_Boolean_create = _pytrch.Parameter_Boolean_create

def Parameter_Boolean_setValue(*args):
  return _pytrch.Parameter_Boolean_setValue(*args)
Parameter_Boolean_setValue = _pytrch.Parameter_Boolean_setValue

def Parameter_Boolean_List_create(*args):
  return _pytrch.Parameter_Boolean_List_create(*args)
Parameter_Boolean_List_create = _pytrch.Parameter_Boolean_List_create

def Parameter_Boolean_List_getSize(*args):
  return _pytrch.Parameter_Boolean_List_getSize(*args)
Parameter_Boolean_List_getSize = _pytrch.Parameter_Boolean_List_getSize

def Parameter_Boolean_List_getValue(*args):
  return _pytrch.Parameter_Boolean_List_getValue(*args)
Parameter_Boolean_List_getValue = _pytrch.Parameter_Boolean_List_getValue

def Parameter_Boolean_List_setValue(*args):
  return _pytrch.Parameter_Boolean_List_setValue(*args)
Parameter_Boolean_List_setValue = _pytrch.Parameter_Boolean_List_setValue

def Parameter_Buffer_create(*args):
  return _pytrch.Parameter_Buffer_create(*args)
Parameter_Buffer_create = _pytrch.Parameter_Buffer_create

def Parameter_Buffer_setValue(*args):
  return _pytrch.Parameter_Buffer_setValue(*args)
Parameter_Buffer_setValue = _pytrch.Parameter_Buffer_setValue

def Parameter_Buffer_List_create(*args):
  return _pytrch.Parameter_Buffer_List_create(*args)
Parameter_Buffer_List_create = _pytrch.Parameter_Buffer_List_create

def Parameter_Buffer_List_getSize(*args):
  return _pytrch.Parameter_Buffer_List_getSize(*args)
Parameter_Buffer_List_getSize = _pytrch.Parameter_Buffer_List_getSize

def Parameter_Buffer_List_getValue(*args):
  return _pytrch.Parameter_Buffer_List_getValue(*args)
Parameter_Buffer_List_getValue = _pytrch.Parameter_Buffer_List_getValue

def Parameter_Buffer_List_setValue(*args):
  return _pytrch.Parameter_Buffer_List_setValue(*args)
Parameter_Buffer_List_setValue = _pytrch.Parameter_Buffer_List_setValue

def Parameter_IPv4_create(*args):
  return _pytrch.Parameter_IPv4_create(*args)
Parameter_IPv4_create = _pytrch.Parameter_IPv4_create

def Parameter_IPv4_setValue(*args):
  return _pytrch.Parameter_IPv4_setValue(*args)
Parameter_IPv4_setValue = _pytrch.Parameter_IPv4_setValue

def Parameter_IPv4_List_create(*args):
  return _pytrch.Parameter_IPv4_List_create(*args)
Parameter_IPv4_List_create = _pytrch.Parameter_IPv4_List_create

def Parameter_IPv4_List_getSize(*args):
  return _pytrch.Parameter_IPv4_List_getSize(*args)
Parameter_IPv4_List_getSize = _pytrch.Parameter_IPv4_List_getSize

def Parameter_IPv4_List_getValue(*args):
  return _pytrch.Parameter_IPv4_List_getValue(*args)
Parameter_IPv4_List_getValue = _pytrch.Parameter_IPv4_List_getValue

def Parameter_IPv4_List_setValue(*args):
  return _pytrch.Parameter_IPv4_List_setValue(*args)
Parameter_IPv4_List_setValue = _pytrch.Parameter_IPv4_List_setValue

def Parameter_IPv6_create(*args):
  return _pytrch.Parameter_IPv6_create(*args)
Parameter_IPv6_create = _pytrch.Parameter_IPv6_create

def Parameter_IPv6_setValue(*args):
  return _pytrch.Parameter_IPv6_setValue(*args)
Parameter_IPv6_setValue = _pytrch.Parameter_IPv6_setValue

def Parameter_IPv6_List_create(*args):
  return _pytrch.Parameter_IPv6_List_create(*args)
Parameter_IPv6_List_create = _pytrch.Parameter_IPv6_List_create

def Parameter_IPv6_List_getSize(*args):
  return _pytrch.Parameter_IPv6_List_getSize(*args)
Parameter_IPv6_List_getSize = _pytrch.Parameter_IPv6_List_getSize

def Parameter_IPv6_List_getValue(*args):
  return _pytrch.Parameter_IPv6_List_getValue(*args)
Parameter_IPv6_List_getValue = _pytrch.Parameter_IPv6_List_getValue

def Parameter_IPv6_List_setValue(*args):
  return _pytrch.Parameter_IPv6_List_setValue(*args)
Parameter_IPv6_List_setValue = _pytrch.Parameter_IPv6_List_setValue

def Parameter_LocalFile_create(*args):
  return _pytrch.Parameter_LocalFile_create(*args)
Parameter_LocalFile_create = _pytrch.Parameter_LocalFile_create

def Parameter_LocalFile_setValue(*args):
  return _pytrch.Parameter_LocalFile_setValue(*args)
Parameter_LocalFile_setValue = _pytrch.Parameter_LocalFile_setValue

def Parameter_LocalFile_List_create(*args):
  return _pytrch.Parameter_LocalFile_List_create(*args)
Parameter_LocalFile_List_create = _pytrch.Parameter_LocalFile_List_create

def Parameter_LocalFile_List_getSize(*args):
  return _pytrch.Parameter_LocalFile_List_getSize(*args)
Parameter_LocalFile_List_getSize = _pytrch.Parameter_LocalFile_List_getSize

def Parameter_LocalFile_List_getValue(*args):
  return _pytrch.Parameter_LocalFile_List_getValue(*args)
Parameter_LocalFile_List_getValue = _pytrch.Parameter_LocalFile_List_getValue

def Parameter_LocalFile_List_setValue(*args):
  return _pytrch.Parameter_LocalFile_List_setValue(*args)
Parameter_LocalFile_List_setValue = _pytrch.Parameter_LocalFile_List_setValue

def Parameter_Port_setValue(*args):
  return _pytrch.Parameter_Port_setValue(*args)
Parameter_Port_setValue = _pytrch.Parameter_Port_setValue

def Parameter_Port_List_getSize(*args):
  return _pytrch.Parameter_Port_List_getSize(*args)
Parameter_Port_List_getSize = _pytrch.Parameter_Port_List_getSize

def Parameter_Port_List_getValue(*args):
  return _pytrch.Parameter_Port_List_getValue(*args)
Parameter_Port_List_getValue = _pytrch.Parameter_Port_List_getValue

def Parameter_Port_List_setValue(*args):
  return _pytrch.Parameter_Port_List_setValue(*args)
Parameter_Port_List_setValue = _pytrch.Parameter_Port_List_setValue

def Parameter_S8_create(*args):
  return _pytrch.Parameter_S8_create(*args)
Parameter_S8_create = _pytrch.Parameter_S8_create

def Parameter_S8_setValue(*args):
  return _pytrch.Parameter_S8_setValue(*args)
Parameter_S8_setValue = _pytrch.Parameter_S8_setValue

def Parameter_S8_List_create(*args):
  return _pytrch.Parameter_S8_List_create(*args)
Parameter_S8_List_create = _pytrch.Parameter_S8_List_create

def Parameter_S8_List_getSize(*args):
  return _pytrch.Parameter_S8_List_getSize(*args)
Parameter_S8_List_getSize = _pytrch.Parameter_S8_List_getSize

def Parameter_S8_List_getValue(*args):
  return _pytrch.Parameter_S8_List_getValue(*args)
Parameter_S8_List_getValue = _pytrch.Parameter_S8_List_getValue

def Parameter_S8_List_setValue(*args):
  return _pytrch.Parameter_S8_List_setValue(*args)
Parameter_S8_List_setValue = _pytrch.Parameter_S8_List_setValue

def Parameter_S16_create(*args):
  return _pytrch.Parameter_S16_create(*args)
Parameter_S16_create = _pytrch.Parameter_S16_create

def Parameter_S16_setValue(*args):
  return _pytrch.Parameter_S16_setValue(*args)
Parameter_S16_setValue = _pytrch.Parameter_S16_setValue

def Parameter_S16_List_create(*args):
  return _pytrch.Parameter_S16_List_create(*args)
Parameter_S16_List_create = _pytrch.Parameter_S16_List_create

def Parameter_S16_List_getSize(*args):
  return _pytrch.Parameter_S16_List_getSize(*args)
Parameter_S16_List_getSize = _pytrch.Parameter_S16_List_getSize

def Parameter_S16_List_getValue(*args):
  return _pytrch.Parameter_S16_List_getValue(*args)
Parameter_S16_List_getValue = _pytrch.Parameter_S16_List_getValue

def Parameter_S16_List_setValue(*args):
  return _pytrch.Parameter_S16_List_setValue(*args)
Parameter_S16_List_setValue = _pytrch.Parameter_S16_List_setValue

def Parameter_S32_create(*args):
  return _pytrch.Parameter_S32_create(*args)
Parameter_S32_create = _pytrch.Parameter_S32_create

def Parameter_S32_setValue(*args):
  return _pytrch.Parameter_S32_setValue(*args)
Parameter_S32_setValue = _pytrch.Parameter_S32_setValue

def Parameter_S32_List_create(*args):
  return _pytrch.Parameter_S32_List_create(*args)
Parameter_S32_List_create = _pytrch.Parameter_S32_List_create

def Parameter_S32_List_getSize(*args):
  return _pytrch.Parameter_S32_List_getSize(*args)
Parameter_S32_List_getSize = _pytrch.Parameter_S32_List_getSize

def Parameter_S32_List_getValue(*args):
  return _pytrch.Parameter_S32_List_getValue(*args)
Parameter_S32_List_getValue = _pytrch.Parameter_S32_List_getValue

def Parameter_S32_List_setValue(*args):
  return _pytrch.Parameter_S32_List_setValue(*args)
Parameter_S32_List_setValue = _pytrch.Parameter_S32_List_setValue

def Parameter_S64_create(*args):
  return _pytrch.Parameter_S64_create(*args)
Parameter_S64_create = _pytrch.Parameter_S64_create

def Parameter_S64_setValue(*args):
  return _pytrch.Parameter_S64_setValue(*args)
Parameter_S64_setValue = _pytrch.Parameter_S64_setValue

def Parameter_S64_List_create(*args):
  return _pytrch.Parameter_S64_List_create(*args)
Parameter_S64_List_create = _pytrch.Parameter_S64_List_create

def Parameter_S64_List_getSize(*args):
  return _pytrch.Parameter_S64_List_getSize(*args)
Parameter_S64_List_getSize = _pytrch.Parameter_S64_List_getSize

def Parameter_S64_List_getValue(*args):
  return _pytrch.Parameter_S64_List_getValue(*args)
Parameter_S64_List_getValue = _pytrch.Parameter_S64_List_getValue

def Parameter_S64_List_setValue(*args):
  return _pytrch.Parameter_S64_List_setValue(*args)
Parameter_S64_List_setValue = _pytrch.Parameter_S64_List_setValue

def Parameter_Socket_create(*args):
  return _pytrch.Parameter_Socket_create(*args)
Parameter_Socket_create = _pytrch.Parameter_Socket_create

def Parameter_Socket_setValue(*args):
  return _pytrch.Parameter_Socket_setValue(*args)
Parameter_Socket_setValue = _pytrch.Parameter_Socket_setValue

def Parameter_Socket_List_create(*args):
  return _pytrch.Parameter_Socket_List_create(*args)
Parameter_Socket_List_create = _pytrch.Parameter_Socket_List_create

def Parameter_Socket_List_getSize(*args):
  return _pytrch.Parameter_Socket_List_getSize(*args)
Parameter_Socket_List_getSize = _pytrch.Parameter_Socket_List_getSize

def Parameter_Socket_List_getValue(*args):
  return _pytrch.Parameter_Socket_List_getValue(*args)
Parameter_Socket_List_getValue = _pytrch.Parameter_Socket_List_getValue

def Parameter_Socket_List_setValue(*args):
  return _pytrch.Parameter_Socket_List_setValue(*args)
Parameter_Socket_List_setValue = _pytrch.Parameter_Socket_List_setValue

def Parameter_String_create(*args):
  return _pytrch.Parameter_String_create(*args)
Parameter_String_create = _pytrch.Parameter_String_create

def Parameter_String_setValue(*args):
  return _pytrch.Parameter_String_setValue(*args)
Parameter_String_setValue = _pytrch.Parameter_String_setValue

def Parameter_String_List_create(*args):
  return _pytrch.Parameter_String_List_create(*args)
Parameter_String_List_create = _pytrch.Parameter_String_List_create

def Parameter_String_List_getSize(*args):
  return _pytrch.Parameter_String_List_getSize(*args)
Parameter_String_List_getSize = _pytrch.Parameter_String_List_getSize

def Parameter_String_List_getValue(*args):
  return _pytrch.Parameter_String_List_getValue(*args)
Parameter_String_List_getValue = _pytrch.Parameter_String_List_getValue

def Parameter_String_List_setValue(*args):
  return _pytrch.Parameter_String_List_setValue(*args)
Parameter_String_List_setValue = _pytrch.Parameter_String_List_setValue

def Parameter_TcpPort_create(*args):
  return _pytrch.Parameter_TcpPort_create(*args)
Parameter_TcpPort_create = _pytrch.Parameter_TcpPort_create

def Parameter_TcpPort_List_create(*args):
  return _pytrch.Parameter_TcpPort_List_create(*args)
Parameter_TcpPort_List_create = _pytrch.Parameter_TcpPort_List_create

def Parameter_U8_create(*args):
  return _pytrch.Parameter_U8_create(*args)
Parameter_U8_create = _pytrch.Parameter_U8_create

def Parameter_U8_setValue(*args):
  return _pytrch.Parameter_U8_setValue(*args)
Parameter_U8_setValue = _pytrch.Parameter_U8_setValue

def Parameter_U8_List_create(*args):
  return _pytrch.Parameter_U8_List_create(*args)
Parameter_U8_List_create = _pytrch.Parameter_U8_List_create

def Parameter_U8_List_getSize(*args):
  return _pytrch.Parameter_U8_List_getSize(*args)
Parameter_U8_List_getSize = _pytrch.Parameter_U8_List_getSize

def Parameter_U8_List_getValue(*args):
  return _pytrch.Parameter_U8_List_getValue(*args)
Parameter_U8_List_getValue = _pytrch.Parameter_U8_List_getValue

def Parameter_U8_List_setValue(*args):
  return _pytrch.Parameter_U8_List_setValue(*args)
Parameter_U8_List_setValue = _pytrch.Parameter_U8_List_setValue

def Parameter_U16_create(*args):
  return _pytrch.Parameter_U16_create(*args)
Parameter_U16_create = _pytrch.Parameter_U16_create

def Parameter_U16_setValue(*args):
  return _pytrch.Parameter_U16_setValue(*args)
Parameter_U16_setValue = _pytrch.Parameter_U16_setValue

def Parameter_U16_List_create(*args):
  return _pytrch.Parameter_U16_List_create(*args)
Parameter_U16_List_create = _pytrch.Parameter_U16_List_create

def Parameter_U16_List_getSize(*args):
  return _pytrch.Parameter_U16_List_getSize(*args)
Parameter_U16_List_getSize = _pytrch.Parameter_U16_List_getSize

def Parameter_U16_List_getValue(*args):
  return _pytrch.Parameter_U16_List_getValue(*args)
Parameter_U16_List_getValue = _pytrch.Parameter_U16_List_getValue

def Parameter_U16_List_setValue(*args):
  return _pytrch.Parameter_U16_List_setValue(*args)
Parameter_U16_List_setValue = _pytrch.Parameter_U16_List_setValue

def Parameter_U32_create(*args):
  return _pytrch.Parameter_U32_create(*args)
Parameter_U32_create = _pytrch.Parameter_U32_create

def Parameter_U32_setValue(*args):
  return _pytrch.Parameter_U32_setValue(*args)
Parameter_U32_setValue = _pytrch.Parameter_U32_setValue

def Parameter_U32_List_create(*args):
  return _pytrch.Parameter_U32_List_create(*args)
Parameter_U32_List_create = _pytrch.Parameter_U32_List_create

def Parameter_U32_List_getSize(*args):
  return _pytrch.Parameter_U32_List_getSize(*args)
Parameter_U32_List_getSize = _pytrch.Parameter_U32_List_getSize

def Parameter_U32_List_getValue(*args):
  return _pytrch.Parameter_U32_List_getValue(*args)
Parameter_U32_List_getValue = _pytrch.Parameter_U32_List_getValue

def Parameter_U32_List_setValue(*args):
  return _pytrch.Parameter_U32_List_setValue(*args)
Parameter_U32_List_setValue = _pytrch.Parameter_U32_List_setValue

def Parameter_U64_create(*args):
  return _pytrch.Parameter_U64_create(*args)
Parameter_U64_create = _pytrch.Parameter_U64_create

def Parameter_U64_setValue(*args):
  return _pytrch.Parameter_U64_setValue(*args)
Parameter_U64_setValue = _pytrch.Parameter_U64_setValue

def Parameter_U64_List_create(*args):
  return _pytrch.Parameter_U64_List_create(*args)
Parameter_U64_List_create = _pytrch.Parameter_U64_List_create

def Parameter_U64_List_getSize(*args):
  return _pytrch.Parameter_U64_List_getSize(*args)
Parameter_U64_List_getSize = _pytrch.Parameter_U64_List_getSize

def Parameter_U64_List_getValue(*args):
  return _pytrch.Parameter_U64_List_getValue(*args)
Parameter_U64_List_getValue = _pytrch.Parameter_U64_List_getValue

def Parameter_U64_List_setValue(*args):
  return _pytrch.Parameter_U64_List_setValue(*args)
Parameter_U64_List_setValue = _pytrch.Parameter_U64_List_setValue

def Parameter_UdpPort_create(*args):
  return _pytrch.Parameter_UdpPort_create(*args)
Parameter_UdpPort_create = _pytrch.Parameter_UdpPort_create

def Parameter_UdpPort_List_create(*args):
  return _pytrch.Parameter_UdpPort_List_create(*args)
Parameter_UdpPort_List_create = _pytrch.Parameter_UdpPort_List_create

def Parameter_UString_create(*args):
  return _pytrch.Parameter_UString_create(*args)
Parameter_UString_create = _pytrch.Parameter_UString_create

def Parameter_UString_setValue(*args):
  return _pytrch.Parameter_UString_setValue(*args)
Parameter_UString_setValue = _pytrch.Parameter_UString_setValue

def Parameter_UString_List_create(*args):
  return _pytrch.Parameter_UString_List_create(*args)
Parameter_UString_List_create = _pytrch.Parameter_UString_List_create

def Parameter_UString_List_getSize(*args):
  return _pytrch.Parameter_UString_List_getSize(*args)
Parameter_UString_List_getSize = _pytrch.Parameter_UString_List_getSize

def Parameter_UString_List_getValue(*args):
  return _pytrch.Parameter_UString_List_getValue(*args)
Parameter_UString_List_getValue = _pytrch.Parameter_UString_List_getValue

def Parameter_UString_List_setValue(*args):
  return _pytrch.Parameter_UString_List_setValue(*args)
Parameter_UString_List_setValue = _pytrch.Parameter_UString_List_setValue

def Paramgroup_addParamchoice(*args):
  return _pytrch.Paramgroup_addParamchoice(*args)
Paramgroup_addParamchoice = _pytrch.Paramgroup_addParamchoice

def Paramgroup_addParameter(*args):
  return _pytrch.Paramgroup_addParameter(*args)
Paramgroup_addParameter = _pytrch.Paramgroup_addParameter

def Paramgroup_create(*args):
  return _pytrch.Paramgroup_create(*args)
Paramgroup_create = _pytrch.Paramgroup_create

def Paramgroup_delete(*args):
  return _pytrch.Paramgroup_delete(*args)
Paramgroup_delete = _pytrch.Paramgroup_delete

def Paramgroup_getDescription(*args):
  return _pytrch.Paramgroup_getDescription(*args)
Paramgroup_getDescription = _pytrch.Paramgroup_getDescription

def Paramgroup_getName(*args):
  return _pytrch.Paramgroup_getName(*args)
Paramgroup_getName = _pytrch.Paramgroup_getName

def Paramgroup_getNumParamchoices(*args):
  return _pytrch.Paramgroup_getNumParamchoices(*args)
Paramgroup_getNumParamchoices = _pytrch.Paramgroup_getNumParamchoices

def Paramgroup_getNumParameters(*args):
  return _pytrch.Paramgroup_getNumParameters(*args)
Paramgroup_getNumParameters = _pytrch.Paramgroup_getNumParameters

def Paramgroup_getParamchoice(*args):
  return _pytrch.Paramgroup_getParamchoice(*args)
Paramgroup_getParamchoice = _pytrch.Paramgroup_getParamchoice

def Paramgroup_getParameter(*args):
  return _pytrch.Paramgroup_getParameter(*args)
Paramgroup_getParameter = _pytrch.Paramgroup_getParameter

def Paramgroup_isValid(*args):
  return _pytrch.Paramgroup_isValid(*args)
Paramgroup_isValid = _pytrch.Paramgroup_isValid

def Paramgroup_matchName(*args):
  return _pytrch.Paramgroup_matchName(*args)
Paramgroup_matchName = _pytrch.Paramgroup_matchName

def Paramgroup_removeParameter(*args):
  return _pytrch.Paramgroup_removeParameter(*args)
Paramgroup_removeParameter = _pytrch.Paramgroup_removeParameter

def List_format():
  return _pytrch.List_format()
List_format = _pytrch.List_format

def Scalar_format():
  return _pytrch.Scalar_format()
Scalar_format = _pytrch.Scalar_format

def Boolean_type():
  return _pytrch.Boolean_type()
Boolean_type = _pytrch.Boolean_type

def Buffer_type():
  return _pytrch.Buffer_type()
Buffer_type = _pytrch.Buffer_type

def IPv4_type():
  return _pytrch.IPv4_type()
IPv4_type = _pytrch.IPv4_type

def IPv6_type():
  return _pytrch.IPv6_type()
IPv6_type = _pytrch.IPv6_type

def LocalFile_type():
  return _pytrch.LocalFile_type()
LocalFile_type = _pytrch.LocalFile_type

def S8_type():
  return _pytrch.S8_type()
S8_type = _pytrch.S8_type

def S16_type():
  return _pytrch.S16_type()
S16_type = _pytrch.S16_type

def S32_type():
  return _pytrch.S32_type()
S32_type = _pytrch.S32_type

def S64_type():
  return _pytrch.S64_type()
S64_type = _pytrch.S64_type

def Socket_type():
  return _pytrch.Socket_type()
Socket_type = _pytrch.Socket_type

def String_type():
  return _pytrch.String_type()
String_type = _pytrch.String_type

def TcpPort_type():
  return _pytrch.TcpPort_type()
TcpPort_type = _pytrch.TcpPort_type

def U8_type():
  return _pytrch.U8_type()
U8_type = _pytrch.U8_type

def U16_type():
  return _pytrch.U16_type()
U16_type = _pytrch.U16_type

def U32_type():
  return _pytrch.U32_type()
U32_type = _pytrch.U32_type

def U64_type():
  return _pytrch.U64_type()
U64_type = _pytrch.U64_type

def UdpPort_type():
  return _pytrch.UdpPort_type()
UdpPort_type = _pytrch.UdpPort_type

def UString_type():
  return _pytrch.UString_type()
UString_type = _pytrch.UString_type

def Boolean_marshal(*args):
  return _pytrch.Boolean_marshal(*args)
Boolean_marshal = _pytrch.Boolean_marshal

def Boolean_List_marshal(*args):
  return _pytrch.Boolean_List_marshal(*args)
Boolean_List_marshal = _pytrch.Boolean_List_marshal

def Buffer_marshal(*args):
  return _pytrch.Buffer_marshal(*args)
Buffer_marshal = _pytrch.Buffer_marshal

def Buffer_List_marshal(*args):
  return _pytrch.Buffer_List_marshal(*args)
Buffer_List_marshal = _pytrch.Buffer_List_marshal

def IPv4_marshal(*args):
  return _pytrch.IPv4_marshal(*args)
IPv4_marshal = _pytrch.IPv4_marshal

def IPv4_List_marshal(*args):
  return _pytrch.IPv4_List_marshal(*args)
IPv4_List_marshal = _pytrch.IPv4_List_marshal

def IPv6_marshal(*args):
  return _pytrch.IPv6_marshal(*args)
IPv6_marshal = _pytrch.IPv6_marshal

def IPv6_List_marshal(*args):
  return _pytrch.IPv6_List_marshal(*args)
IPv6_List_marshal = _pytrch.IPv6_List_marshal

def LocalFile_marshal(*args):
  return _pytrch.LocalFile_marshal(*args)
LocalFile_marshal = _pytrch.LocalFile_marshal

def LocalFile_List_marshal(*args):
  return _pytrch.LocalFile_List_marshal(*args)
LocalFile_List_marshal = _pytrch.LocalFile_List_marshal

def Port_marshal(*args):
  return _pytrch.Port_marshal(*args)
Port_marshal = _pytrch.Port_marshal

def Port_List_marshal(*args):
  return _pytrch.Port_List_marshal(*args)
Port_List_marshal = _pytrch.Port_List_marshal

def S8_marshal(*args):
  return _pytrch.S8_marshal(*args)
S8_marshal = _pytrch.S8_marshal

def S8_List_marshal(*args):
  return _pytrch.S8_List_marshal(*args)
S8_List_marshal = _pytrch.S8_List_marshal

def S16_marshal(*args):
  return _pytrch.S16_marshal(*args)
S16_marshal = _pytrch.S16_marshal

def S16_List_marshal(*args):
  return _pytrch.S16_List_marshal(*args)
S16_List_marshal = _pytrch.S16_List_marshal

def S32_marshal(*args):
  return _pytrch.S32_marshal(*args)
S32_marshal = _pytrch.S32_marshal

def S32_List_marshal(*args):
  return _pytrch.S32_List_marshal(*args)
S32_List_marshal = _pytrch.S32_List_marshal

def S64_marshal(*args):
  return _pytrch.S64_marshal(*args)
S64_marshal = _pytrch.S64_marshal

def S64_List_marshal(*args):
  return _pytrch.S64_List_marshal(*args)
S64_List_marshal = _pytrch.S64_List_marshal

def Socket_marshal(*args):
  return _pytrch.Socket_marshal(*args)
Socket_marshal = _pytrch.Socket_marshal

def Socket_List_marshal(*args):
  return _pytrch.Socket_List_marshal(*args)
Socket_List_marshal = _pytrch.Socket_List_marshal

def String_marshal(*args):
  return _pytrch.String_marshal(*args)
String_marshal = _pytrch.String_marshal

def String_List_marshal(*args):
  return _pytrch.String_List_marshal(*args)
String_List_marshal = _pytrch.String_List_marshal

def U8_marshal(*args):
  return _pytrch.U8_marshal(*args)
U8_marshal = _pytrch.U8_marshal

def U8_List_marshal(*args):
  return _pytrch.U8_List_marshal(*args)
U8_List_marshal = _pytrch.U8_List_marshal

def U16_marshal(*args):
  return _pytrch.U16_marshal(*args)
U16_marshal = _pytrch.U16_marshal

def U16_List_marshal(*args):
  return _pytrch.U16_List_marshal(*args)
U16_List_marshal = _pytrch.U16_List_marshal

def U32_marshal(*args):
  return _pytrch.U32_marshal(*args)
U32_marshal = _pytrch.U32_marshal

def U32_List_marshal(*args):
  return _pytrch.U32_List_marshal(*args)
U32_List_marshal = _pytrch.U32_List_marshal

def U64_marshal(*args):
  return _pytrch.U64_marshal(*args)
U64_marshal = _pytrch.U64_marshal

def U64_List_marshal(*args):
  return _pytrch.U64_List_marshal(*args)
U64_List_marshal = _pytrch.U64_List_marshal

def UString_marshal(*args):
  return _pytrch.UString_marshal(*args)
UString_marshal = _pytrch.UString_marshal

def UString_List_marshal(*args):
  return _pytrch.UString_List_marshal(*args)
UString_List_marshal = _pytrch.UString_List_marshal


