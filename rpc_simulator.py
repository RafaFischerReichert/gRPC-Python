import grpc
import calculator_pb2
import calculator_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = calculator_pb2_grpc.CalculatorStub(channel)

request = calculator_pb2.AddRequest(x=2, y=3)
response = stub.Add(request)

print("Result 1:", response.result)

request = calculator_pb2.MultiplyRequest(x=4, y=5)
response = stub.Multiply(request)

print("Result 2:", response.result)