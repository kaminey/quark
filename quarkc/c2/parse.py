from .match import *
from .ast import *
from .parser import Parser
from .exceptions import ParseError
from parsimonious import ParseError as GParseError

@match(AST, object, opt(object))
def traverse(node, visit, leave=None):
    visit(node)
    for c in node.children:
        if c is not None:
            traverse(c, visit, leave)
    if leave:
        leave(node)

@match(AST)
def traversal(node):
    yield node
    for c in node.children:
        if c is not None:
            for n in traversal(c):
                yield n

@match([many(Package)])
def traversal(pkgs):
    for p in pkgs:
        for n in traversal(p):
            yield n

@match(AST)
def postorder_traversal(node):
    for c in node.children:
        if c is not None:
            for n in postorder_traversal(c):
                yield n
    yield node

@match([many(Package)])
def postorder_traversal(pkgs):
    for p in pkgs:
        for n in postorder_traversal(p):
            yield n

@match(File)
def wire(file):
    path = []

    def visit(n):
        n.file = file
        if path:
            n.parent = path[-1]
        else:
            n.parent = None

        if not hasattr(n, "_marked"):
            n._marked = True
            n.line, n.column = n.parent.line, n.parent.column

        path.append(n)

    def leave(n):
        path.pop()

    traverse(file, visit, leave)
    return file

@match(basestring, basestring)
def parse(name, text):
    # XXX: need to handle version here
    p = Parser()
    p._filename = name
    try:
        return wire(p.parse(text))
    except GParseError, e:
        location = '%s:%s:%s: ' % (name, e.line(), e.column())
        raise ParseError("%s%s" % (location, e))
