# pattern prototype реализован в питоне с помощью copy.deepcopy
import copy


class Original:
    pass


original = Original()
prototype = copy.deepcopy(original)

print(original is prototype)


# либо наследуя класс:

class PrototypeMixin:
    # прототип

    def clone(self):
        return copy.deepcopy(self)


class Tester(PrototypeMixin):
    pass


a = Tester()
a1 = a.clone()

print(a is a1)
