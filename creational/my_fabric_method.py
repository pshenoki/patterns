from abc import abstractmethod, ABC


class Transport(ABC):

    @abstractmethod
    def run(self):
        pass


class Auto(Transport):

    def run(self):
        return 'run on road'


class Plan(Transport):

    def run(self):
        return 'run on air'


class Ship(Transport):

    def run(self):
        return 'run on sea'


class TransportFactory:
    transport_dict = {
                    'auto': Auto(),
                    'plan': Plan(),
                    'ship': Ship()
                     }

    def create_transport(self, transport):
        return self.transport_dict[transport]


if __name__ == '__main__':
    factory = TransportFactory()
    print(factory.create_transport('auto').run())
    print(factory.create_transport('plan').run())
    print(factory.create_transport('ship').run())
