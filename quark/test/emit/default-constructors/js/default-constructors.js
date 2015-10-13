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

// CLASS A

function A(name) {
    this.__init_fields__();
    (this).name = name;
}
exports.A = A;

function A__init_fields__() {
    this.name = null;
}
A.prototype.__init_fields__ = A__init_fields__;


// CLASS B
function B(name) {
    B.super_.call(this, name);
}
exports.B = B;
_Q_util.inherits(B, A);

function B__init_fields__() {
    A.prototype.__init_fields__.call(this);
}
B.prototype.__init_fields__ = B__init_fields__;

function B_greet() {
    console.log(_Q_toString(("Hello, my name is ") + ((this).name)));
}
B.prototype.greet = B_greet;

// CLASS C

function C(name) {
    C.super_.call(this, ("C") + (name));
}
exports.C = C;
_Q_util.inherits(C, A);

function C__init_fields__() {
    A.prototype.__init_fields__.call(this);
}
C.prototype.__init_fields__ = C__init_fields__;

function C_greet() {
    console.log(_Q_toString(("Greetings, my name is ") + ((this).name)));
}
C.prototype.greet = C_greet;

function main() {
    var b = new B("Bob");
    (b).greet();
    var c = new C("arole");
    (c).greet();
}
exports.main = main;

main();