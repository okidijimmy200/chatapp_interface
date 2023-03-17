from app.interfaces import StreamingServiceInterface, UserInputDeliveryReportInterface
from confluent_kafka import Producer, Consumer
from models.models import PublisherRequest


class StreamingService(StreamingServiceInterface):

    def __init__(self, user_input: UserInputDeliveryReportInterface) -> None:
        self.user_input = user_input
    
    def publisher(self, req: PublisherRequest) -> str:
        try:
            messg = self.user_input.read_message()
            callback = self.user_input.delivery_report

            p = Producer({'bootstrap.servers': req.server})
            p.poll(0)
            p.produce(req.channel, messg, callback=callback)
            result = p.flush()
            return result

        except  Exception as e:
            return (
                f"Failed to send message:" 
                + f"{type(e).__name__} {str(e)}"
            )
        
    def subscriber(self, channel, start_from, server, group, running):
        try:
            c = Consumer({
            'bootstrap.servers': server,
            'group.id': group,
            'auto.offset.reset': start_from
            })

            c.subscribe([channel])


            while running['running']:
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