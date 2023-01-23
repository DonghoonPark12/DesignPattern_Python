class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."

class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """
    """
    Adaptee는 client 코드가 사용전에 조정(?)하는 역할을 한다.
    """
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Target, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """
    """
    Adapter는 다중 상속을 통해 Adaptee의 인터페이스가 Target 인터페이스와 호환되도록 한다.
    """
    def request(self) -> str: # 매소드 오버라이딩
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"

def client_code(target: "Target") -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.request(), end="")

if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target) # client_code는 Target 클래스 객체를 입력으로 받음
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")
    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()  # 다중 상속
    client_code(adapter) # client_code는 Target 클래스를 상속받은 Adapter 클래스 객체를 입력으로 받을 수 있다.
                         # Adapter 클래스의 오버라이딩 된 매소드 .request()를 호출한다.
"""
Client: I can work just fine with the Target objects:
Target: The default target's behavior.

Client: The Adaptee class has a weird interface. See, I don't understand it:
Adaptee: .eetpadA eht fo roivaheb laicepS

Client: But I can work with it via the Adapter:
Adapter: (TRANSLATED) Special behavior of the Adaptee.
"""