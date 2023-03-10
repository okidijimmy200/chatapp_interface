from interfaces import StreamingServiceInterface
from confluent_kafka import Producer, Consumer
from interfaces import UserInputDeliveryReportInterface

class StreamingService(StreamingServiceInterface):

    def __init__(self,  user_input: UserInputDeliveryReportInterface) -> None:
        self.user_input = user_input
    
    def publisher(self, server, channel, group=None):
        try:
            p = Producer({'bootstrap.servers': server})
            messg = self.user_input.write_message()
            p.poll(0)
            p.produce(channel, messg, callback=self.user_input.delivery_report)

            result = p.flush()
            return result
        except  Exception as e:
            return (
                f"Failed to send message:" 
                + f"{type(e).__name__} {str(e)}"
            )
        
    def subscriber(self, channel, start_from, server, group):
        try:
            c = Consumer({
            'bootstrap.servers': server,
            'group.id': group,
            'auto.offset.reset': start_from
            })

            c.subscribe([channel])

            while True:
                msg = c.poll(1.0)

                if msg is None:
                    continue
                if msg.error():
                    print("Consumer error: {}".format(msg.error()))
                    continue
                
                else:
                    print('Received message: {}'.format(msg.value()))

        except  Exception as e:
            return (
                f"Failed to receive message:" 
                + f"{type(e).__name__} {str(e)}"
            )