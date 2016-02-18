@version("1.2.3") // version is mandatory
namespace interop { // package interop is mandatory
    class Entrypoint { // class Entrypoint is mandatory
        void server(int port) { // port is mandatory constructor parameter
            HelloServlet servlet = HelloServlet();
            servlet.expectRequest()
                .expectMethod("POST")
                .expectUrl("/http_server")
                .expectHeader("X-custom-header", "custom client value")
                .expectBody("client body")
                .check(5.0);
            servlet.serveHTTP("http://127.0.0.1:" + port.toString() + "/http_server");
        }
        void client(int port) {

            TimeoutClient(port)
                .url("/http_server")
                .method("POST")
                .header("X-Custom-Header", "custom client value")
                .body("client body")
                .expectCode(200)
                .expectBody("Hello World!\r\n")
                .expectHeader("X-Custom-Header", "custom value")
                .check(0.5);
        }
    }
////include http_server.qinc
////include common.qinc
}
