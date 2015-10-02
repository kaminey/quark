# Copyright 2015 datawire. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from collections import OrderedDict

# XXX: danger!!! circular import reference hack
import ast
import backend
import java
from .dispatch import overload


class JavaScript(backend.Backend):

    def __init__(self):
        backend.Backend.__init__(self, "js")
        self.dfnr = JSDefinitionRenderer()
        self.header = """\
var _Q_util = require("util");
function _Q_toString(value) {
    if (value === null) {
        return "null";
    }
    if (Array.isArray(value)) {
        return "[" + value.map(_Q_toString).join(", ") + "]";
    }
    return value.toString();
}

//
"""

    def write(self, target):
        if not os.path.exists(target):
            os.makedirs(target)
        for name, content in self.files.items():
            path = os.path.join(target, name)
            dir = os.path.dirname(path)
            if not os.path.exists(dir):
                os.makedirs(dir)
            open(path, "wb").write(content)
            print "wrote", path

    def imports(self, packages):
        result = "\n".join(["var %s = require('./%s');" % (pkg, pkg) for pkg in packages.keys()])
        if result:
            result += "\n"
        return result

    def visit_File(self, file):
        content = "\n".join([d.match(self.dfnr) for d in file.definitions])
        if content.strip() != "":
            fname = os.path.splitext(os.path.basename(file.name))[0]
            #self.files["%s.js" % self.dfnr.namer.get(fname)] = header + content.rstrip() + "\n"
            self.files["%s.js" % fname] = self.header + content.rstrip() + "\n"

    def visit_Package(self, pkg):
        pkg.imports = OrderedDict()
        content = "\n".join([d.match(self.dfnr) for d in pkg.definitions])
        pname = self.dfnr.namer.package(pkg)
        fname = "%s/index.js" % pname.replace(".", "/")
        if fname in self.files:
            self.files[fname] += "\n\n" + self.imports(pkg.imports) + content
        else:
            self.files[fname] = self.header + self.imports(pkg.imports) + content

    def visit_Primitive(self, p):
        pass


class JSDefinitionRenderer(java.DefinitionRenderer):

    def __init__(self):
        self.namer = JSNamer()
        self.stmtr = JSStatementRenderer(self.namer)
        self.fieldr = JSFieldRenderer(self.namer, self.stmtr.exprr)

    def constructors(self, cls):
        return [d for d in cls.definitions if isinstance(d, ast.Method) and d.type is None]

    def match_Package(self, p):
        if isinstance(p.parent, ast.Package):
            p.parent.imports[p.name.match(self.namer)] = True
        return ""

    def match_Class(self, c):
        name = c.name.match(self.namer)
        fields = []
        methods = []
        constructor = None

        if c.base:
            base_class = c.base.match(self.namer)
            fields.append(base_class + ".prototype.__init_fields__.call(this);")
        else:
            base_class = None

        for definition in c.definitions:
            if isinstance(definition, ast.Field):
                fields.append(definition.match(self.fieldr))
            elif not definition.type:
                assert constructor is None
                constructor = definition
            else:
                methods.append(definition.match(self, class_name=name) % dict(class_name=name))

        res = "\n// CLASS %s\n" % name
        if constructor:
            res += constructor.match(self, class_name=name) % dict(class_name=name)
        else:
            res += "function %s() {\n    this.__init_fields__();\n}\n" % name
        res += "exports.%s = %s;\n" % (name, name)
        if base_class:
            res += "_Q_util.inherits(%s, %s);\n" % (name, base_class)

        res += "\nfunction %s__init_fields__() {" % name + java.indent("\n".join(fields)) + "}\n"
        res += "%s.prototype.__init_fields__ = %s__init_fields__;\n" % (name, name)

        res += "\n".join(methods)

        return res

    def match_Function(self, m, class_name=None):
        doc = self.doc(m.annotations)
        name = m.name.match(self.namer)
        params = ", ".join([p.match(self) for p in m.params])
        mods = ""
        header = []
        if isinstance(m, ast.Method):
            if m.type:
                # Method
                new_name = "%s_%s" % (class_name, name)
                trailer = "%s.prototype.%s = %s;" % (class_name, name, new_name)
                name = new_name
            else:
                # Constructor
                header.append("this.__init_fields__();")
                trailer = ""
        else:
            # Function
            trailer = "exports.%s = %s;" % (name, name)
        if m.body is None and not isinstance(m.clazz, ast.Interface):
            mods = mods + " abstract"
        body = " %s" % m.body.match(self.stmtr, header=header) if m.body else ";"
        return "%s%s\nfunction %s(%s)%s\n" % (doc, mods, name, params, body) + trailer

    def match_Macro(self, m, class_name=None):
        return ""

    def match_MethodMacro(self, mm, class_name=None):
        return ""

    def match_Primitive(self, p):
        return ""


class JSFieldRenderer(object):

    def __init__(self, namer, exprr):
        self.namer = namer
        self.exprr = exprr

    def match_Field(self, field):
        name = field.name.match(self.namer)
        if field.value:
            return "this.%s = %s;" % (name, field.value.match(self.exprr))
        else:
            return "this.%s = null;" % name


class JSStatementRenderer(java.StatementRenderer):

    def __init__(self, namer):
        self.namer = namer
        self.exprr = JSExprRenderer(self.namer)

    def maybe_cast(self, type, expr):
        return expr.match(self.exprr)

    def match_Param(self, d):
        name = d.name.match(self.namer)
        if d.value:
            return "%s = %s /* FIXME */" % (name, d.value.match(self.exprr))
        else:
            return name

    def match_Declaration(self, d):
        name = d.name.match(self.namer)
        if d.value:
            return "var %s = %s" % (name, d.value.match(self.exprr))
        else:
            return "var %s" % name

    def match_Assign(self, ass):
        return "%s = %s;" % (ass.lhs.match(self.exprr), ass.rhs.match(self.exprr))

    def match_Block(self, b, header=None):
        header = header or []
        return "{%s}" % java.indent("\n".join(header + [s.match(self) for s in b.statements]))


class JSExprRenderer(java.ExprRenderer):

    def __init__(self, namer):
        java.ExprRenderer.__init__(self, namer)

    @property
    def lang(self):
        return "js"

    @overload(ast.AST)
    def var(self, dfn, v):
        if isinstance(v.definition, ast.Field):
            return "this.%s" % v.match(self.namer)
        else:
            name = v.match(self.namer)
            if isinstance(v.definition, ast.Package):
                v.file.imports[name] = True
            return name

    @overload(ast.Function)
    def var(self, dfn, v):
        pkg = self.namer.package(dfn)
        if pkg:
            return "%s.%s" % (pkg, v.match(self.namer))
        else:
            return "%s" % v.match(self.namer)

    def match_List(self, l):
        return "[%s]" % ", ".join([e.match(self) for e in l.elements])


class JSNamer(java.SubstitutionNamer):

    def __init__(self):
        java.SubstitutionNamer.__init__(self, ({"self": "this", "int": "Number", "List": "Array"}))

    def match_Type(self, t):
        return ".".join([p.match(self) for p in t.path])

    def get(self, name):
        return self.env.get(name, name.replace("-", "_"))