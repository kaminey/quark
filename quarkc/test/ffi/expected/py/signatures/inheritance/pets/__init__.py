from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from builtins import str as unicode

from quark_runtime import *
_lazyImport.plug("inheritance.pets")
import quark.reflect


class Pet(_QObject):
    def _init(self):
        pass
    def __init__(self): self._init()

    def greet(self):
        raise NotImplementedError('`Pet.greet` is an abstract method')

    def _getClass(self):
        return u"inheritance.pets.Pet"

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
Pet.inheritance_pets_Pet_ref = None
class Cat(Pet):
    def _init(self):
        Pet._init(self)

    def __init__(self):
        super(Cat, self).__init__();

    def greet(self):
        _println(u"meow!");

    def _getClass(self):
        return u"inheritance.pets.Cat"

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
Cat.inheritance_pets_Cat_ref = None
class Dog(Pet):
    def _init(self):
        Pet._init(self)

    def __init__(self):
        super(Dog, self).__init__();

    def greet(self):
        _println(u"woof!");

    def _getClass(self):
        return u"inheritance.pets.Dog"

    def _getField(self, name):
        return None

    def _setField(self, name, value):
        pass
Dog.inheritance_pets_Dog_ref = None

def _lazy_import_quark_ffi_signatures_md():
    import quark_ffi_signatures_md
    globals().update(locals())
_lazyImport("import quark_ffi_signatures_md", _lazy_import_quark_ffi_signatures_md)



_lazyImport.pump("inheritance.pets")
