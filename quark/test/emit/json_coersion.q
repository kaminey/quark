void main() {
    JSONObject json = new JSONObject();
    json["string"] = "this is a string";
    json["number"] = 3.14159;
    //json["boolean"] = true;
    String encoded = json.toString();
    print(encoded);
    JSONObject dec = encoded.parseJSON();
    String string = dec["string"];
    float number = dec["number"];
    //bool boolean = dec["boolean"];
    print(string);
    print(number);
    //print(boolean);
}
