// Quark Runtime
/* jshint node: true */

(function () {
    "use strict";

    exports.util = require("util");
    var http = require("http")

    function quark_toString(value) {
        if (value === null) {
            return "null";
        }
        if (Array.isArray(value)) {
            return "[" + value.map(quark_toString).join(", ") + "]";
        }
        return value.toString();
    }
    exports.toString = quark_toString;

    function print(message) {
        console.log(quark_toString(message));
    }
    exports.print = print;

    function modulo(a, b) {
        return (a % b + b) % b;
    }
    exports.modulo = modulo;

    function map_get(m, key) {
        if (m.has(key)) {
            return m.get(key);
        }
        return null;
    }
    exports.map_get = map_get;

    var execSync = require("child_process").execSync;

    function url_get(url) {
        var resBuffer = execSync('curl -s -w "\n\n%{http_code}" ' + url);
        var res = resBuffer.toString("UTF-8");
        if (res.substr(-5) === "\n\n200") {
            return res.substr(0, res.length - 5);
        }
        return "error";
    }
    exports.url_get = url_get;

    function url_get_async(url, cb) {
        var req = http.get(url, function(response) {
            var body = '';
            response.on('data', function(chunk) {
                body += chunk;
            });
            response.on('end', function() {
                cb.callback(body);
            });
        });
        req.on('error', function(e) {
            cb.errback('error');
        });
        req.end();
    }
    exports.url_get_async = url_get_async

    function sleep(seconds) {
        execSync("sleep " + seconds);
    }
    exports.sleep = sleep;

    // CLASS Async
    function Async() {
        this.__init_fields__();
    }
    exports.Async = Async;

    function Async__init_fields__() {}
    Async.prototype.__init_fields__ = Async__init_fields__;

    function Async_callback(result) { /* interface */ }
    Async.prototype.callback = Async_callback;

    function Async_errback(failure) { /* interface */ }
    Async.prototype.errback = Async_errback;


})();
