primitive Object {
    macro int __eq__(Object other) $java{($self).equals($other)}
                                   $py{($self) == ($other)};
    macro int __ne__(Object other) $java{!(($self).equals($other))}
                                   $py{($self) != ($other)};
}

primitive void {}

primitive number {
    macro number __add__(number other) ${($self) + ($other)};
    macro number __sub__(number other) ${($self) - ($other)};
    macro number __mul__(number other) ${($self) * ($other)};
    macro number __div__(number other) ${($self) / ($other)};
    macro number __lt__(number other) ${($self) < ($other)};
    macro number __gt__(number other) ${($self) > ($other)};
}

primitive int extends number {
    macro String toString() $java{Integer.toString($self)}
                            $py{str($self)};
}

primitive long extends number {}

primitive float extends number {
    macro float __div__(float other) $java{($self) / ($other)}
                                     $py{float($self) / float($other)};
    macro String toString() $java{Float.toString($self)}
                            $py{str($self)};
}

primitive String {
    macro String __add__(String other) ${($self) + ($other)};
}

primitive List<T> {
    macro void add(T element) $java{($self).add($element)}
                              $py{($self).append($element)};
    macro T __get__(int index) $java{($self).get($index)}
                               $py{($self)[$index]};
    macro void __set__(int index, T value) $java{($self).set(($index), ($value))}
                                           $py{($self)[$index] = ($value)};
    macro int size() $java{($self).size()}
                     $py{len($self)};
}

primitive Map<K,V> {
    macro void __set__(K key, V value) $java{($self).put(($key), ($value))}
                                       $py{($self)[$key] = ($value)};
    macro V __get__(K key) ${($self).get($key)};
    macro int contains(K key) ${($self).containsKey($key)};
}

macro void print(String msg) $java{System.out.println($msg)}
                             $py{_println($msg)};

macro long now() $java{System.currentTimeMillis()}
                 $py{long(time.time()*1000)};