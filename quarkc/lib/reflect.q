quark *;
namespace quark {
namespace reflect {

    class Class {

        static Map<String,Class> classes = {};

        static Class VOID = new Class("quark.void");
        static Class BOOL = new Class("quark.bool");
        static Class INT = new Class("quark.int");
        static Class LONG = new Class("quark.long");
        static Class FLOAT = new Class("quark.float");
        static Class STRING = new Class("quark.String");
        static Class OBJECT = new Class("quark.Object");

        static Class get(String id) {
            if (!classes.contains(id)) {
                print("Cannot find " + id + " in " + classes.keys().toString());
            }
            return classes[id];
        }

        String id;
        String name;
        List<String> parameters = [];
        List<Field> fields = [];
        List<Method> methods = [];
        List<Class> parents = [];

        Class(String id) {
            self.id = id;
            classes[id] = self;
            self.name = id;
        }

        String getId() {
            return id;
        }

        String getName() {
            return name;
        }

        List<Class> getParameters() {
            List<Class> result = [];
            int idx = 0;
            while (idx < parameters.size()) {
                result.add(Class.get(parameters[idx]));
                idx = idx + 1;
            }
            return result;
        }

        Object construct(List<Object> args) { return null; }

        List<Field> getFields() { return fields; }

        Field getField(String name) {
            int idx = 0;
            while (idx < fields.size()) {
                if (fields[idx].name == name) {
                    return fields[idx];
                }
                idx = idx + 1;
            }
            return null;
        }

        List<Method> getMethods() { return methods; }

        Method getMethod(String name) {
            int idx = 0;
            while (idx < methods.size()) {
                if (methods[idx].name == name) {
                    return methods[idx];
                }
                idx = idx + 1;
            }
            return null;
        }

        bool isSubclassOf(Class anotherClass) {
            if (anotherClass == self) {
                return true;
            }
            int idx = 0;
            while (idx < self.parents.size()) {
                if (self.parents[idx].isSubclassOf(anotherClass)) {
                    return true;
                }
                idx = idx + 1;
            }
            return false;
        }

        @doc("Return whether the given object is an instance of the class or one of its super-classes.")
        bool hasInstance(Object o) {
            return o.getClass().isSubclassOf(self);
        }

        macro JSONObject toJSON() new JSONObject().setString(self.id);
        macro JSONObject __to_JSONObject() self.toJSON();

    }

    macro Class __register__(Class md_ref) $java{$md_ref} $py{None} $rb{nil} $js{null};

    class Field {
        String type;
        String name;

        Field(String type, String name) {
            self.type = type;
            self.name = name;
        }

        Class getType() {
            return Class.get(type);
        }

        String getName() {
            return name;
        }
    }

    class Method {
        String type;
        String name;
        List<String> parameters;

        Method(String type, String name, List<String> parameters) {
            self.type = type;
            self.name = name;
            self.parameters = parameters;
        }

        Class getType() {
            return Class.get(type);
        }

        String getName() {
            return name;
        }

        List<Class> getParameters() {
            List<Class> result = [];
            int idx = 0;
            while (idx < parameters.size()) {
                result.add(Class.get(parameters[idx]));
                idx = idx + 1;
            }
            return result;
        }

        Object invoke(Object object, List<Object> args);
    }

}}
