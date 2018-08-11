# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from observatory.protobuf import observatory_pb2 as observatory_dot_protobuf_dot_observatory__pb2


class TrackingServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RecordMetric = channel.unary_unary(
        '/observatory.protobuf.TrackingService/RecordMetric',
        request_serializer=observatory_dot_protobuf_dot_observatory__pb2.RecordMetricRequest.SerializeToString,
        response_deserializer=observatory_dot_protobuf_dot_observatory__pb2.RecordMetricResponse.FromString,
        )
    self.RecordSessionStart = channel.unary_unary(
        '/observatory.protobuf.TrackingService/RecordSessionStart',
        request_serializer=observatory_dot_protobuf_dot_observatory__pb2.RecordSessionStartRequest.SerializeToString,
        response_deserializer=observatory_dot_protobuf_dot_observatory__pb2.RecordSessionStartResponse.FromString,
        )
    self.RecordSessionCompletion = channel.unary_unary(
        '/observatory.protobuf.TrackingService/RecordSessionCompletion',
        request_serializer=observatory_dot_protobuf_dot_observatory__pb2.RecordSessionCompletionRequest.SerializeToString,
        response_deserializer=observatory_dot_protobuf_dot_observatory__pb2.RecordSessionCompletionResponse.FromString,
        )
    self.RecordSettings = channel.unary_unary(
        '/observatory.protobuf.TrackingService/RecordSettings',
        request_serializer=observatory_dot_protobuf_dot_observatory__pb2.RecordSettingsRequest.SerializeToString,
        response_deserializer=observatory_dot_protobuf_dot_observatory__pb2.RecordSettingsResponse.FromString,
        )


class TrackingServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def RecordMetric(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RecordSessionStart(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RecordSessionCompletion(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RecordSettings(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TrackingServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RecordMetric': grpc.unary_unary_rpc_method_handler(
          servicer.RecordMetric,
          request_deserializer=observatory_dot_protobuf_dot_observatory__pb2.RecordMetricRequest.FromString,
          response_serializer=observatory_dot_protobuf_dot_observatory__pb2.RecordMetricResponse.SerializeToString,
      ),
      'RecordSessionStart': grpc.unary_unary_rpc_method_handler(
          servicer.RecordSessionStart,
          request_deserializer=observatory_dot_protobuf_dot_observatory__pb2.RecordSessionStartRequest.FromString,
          response_serializer=observatory_dot_protobuf_dot_observatory__pb2.RecordSessionStartResponse.SerializeToString,
      ),
      'RecordSessionCompletion': grpc.unary_unary_rpc_method_handler(
          servicer.RecordSessionCompletion,
          request_deserializer=observatory_dot_protobuf_dot_observatory__pb2.RecordSessionCompletionRequest.FromString,
          response_serializer=observatory_dot_protobuf_dot_observatory__pb2.RecordSessionCompletionResponse.SerializeToString,
      ),
      'RecordSettings': grpc.unary_unary_rpc_method_handler(
          servicer.RecordSettings,
          request_deserializer=observatory_dot_protobuf_dot_observatory__pb2.RecordSettingsRequest.FromString,
          response_serializer=observatory_dot_protobuf_dot_observatory__pb2.RecordSettingsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'observatory.protobuf.TrackingService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
