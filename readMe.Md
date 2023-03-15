
A command line chat application in python that uses message broker services of confluent kafka to send and
messages.

Implemented using SOLID principles i.e
S - Single Responsibility Principle
    Made sure each method has a single task. This makes it easier to decouple applications, easening testing and
    improving the overall layout pattern of work.

O  - Open and Closed Principle
    Developed and implemented interfaces that makes it easy to extend the functionality of a service without changing the underlaying structure of the application

L  - Liskov Substitution Principle
    Designed interfaces that make it easy to replace one service with another without breaking the internal
    workings of the application.

I  - Interface Segragation Principle (IS)
    Split Interfaces into 'smaller' interfaces that perform a range of related tasks only i.e Publisher and Subscriber methods in the StreamingService Interface

D - Dependency Inversion
    Implemented abstractions for classes using interfaces. These interfaces act as hand-shakes for connection
    to differnet services which are eventually injected into the application.



to send messages:
>python main.py send --channel mychannel --server localhost:9092 --group mygroup

type a message to send

to receive the message
>python main.py receive --channel mychannel --start_from beginning --server localhost:9092 --group mygroup