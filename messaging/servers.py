from app.interfaces import StreamingServiceInterface, UserInputDeliveryReportInterface
from confluent_kafka import Producer, Consumer
from models.models import PublisherRequest, PublisherResponse, ConsumerRequest, ConsumerResponse


class StreamingService(StreamingServiceInterface):

    def __init__(self, user_input: UserInputDeliveryReportInterface) -> None:
        self.user_input = user_input
    
    def publisher(self, req: PublisherRequest) -> PublisherResponse:
        try:
            messg = self.user_input.read_message()
            callback = self.user_input.delivery_report

            p = Producer({'bootstrap.servers': req.server})
            p.poll(0)
            p.produce(req.channel, messg, callback=callback)
            result = p.flush()
            response = PublisherResponse(result)
            return response.response

        except  Exception as e:
            return (
                f"Failed to send message:" 
                + f"{type(e).__name__} {str(e)}"
            )
        
    def subscriber(self, req: ConsumerRequest) -> ConsumerResponse:
        try:
            c = Consumer({
            'bootstrap.servers': req.server,
            'group.id': req.group,
            'auto.offset.reset': req.start_from
            })

            c.subscribe([req.channel])


            while req.running['running']:
                msg = c.poll(1.0)
                msg_res = ConsumerResponse(msg)

                if msg_res.msg is None:
                    continue
                if msg_res.msg.error():
                    print("Consumer error: {}".format(msg_res.msg.error()))
                    continue
                
                else:
                    print('Received message: {}'.format(msg_res.msg.value()))
        except  Exception as e:
            return (
                f"Failed to receive message:" 
                + f"{type(e).__name__} {str(e)}"
            )