package quark_ffi_signatures_md;

public class interfaces_RazFaz_quark_Object__m3_Method extends quark.reflect.Method implements io.datawire.quark.runtime.QObject {
    public interfaces_RazFaz_quark_Object__m3_Method() {
        super("quark.void", "m3", new java.util.ArrayList(java.util.Arrays.asList(new Object[]{"quark.List<quark.Object>"})));
    }
    public Object invoke(Object object, java.util.ArrayList<Object> args) {
        interfaces.RazFaz<Object> obj = (interfaces.RazFaz<Object>) (object);
        (obj).m3((java.util.ArrayList<Object>) ((args).get(0)));
        return null;
    }
    public String _getClass() {
        return (String) (null);
    }
    public Object _getField(String name) {
        return null;
    }
    public void _setField(String name, Object value) {}
}
