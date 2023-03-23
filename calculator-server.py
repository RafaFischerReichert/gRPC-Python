from concurrent import futures
import grpc
import calculator_pb2
import calculator_pb2_grpc


class Calculator(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.x + request.y
        return calculator_pb2.AddResponse(result=result)

    def Multiply(self, request, context):
        result = request.x * request.y
        return calculator_pb2.MultiplyResponse(result=result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
