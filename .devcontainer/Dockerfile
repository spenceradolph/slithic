# TODO: pick smaller image
FROM ubuntu:22.04

RUN apt-get update
RUN apt-get install -y --no-install-recommends git python3 pip curl gnupg software-properties-common openssh-client build-essential python3-dev libssl-dev

WORKDIR /slithic

# https://github.com/moloch--/sliver-py/issues/28#issuecomment-1469011869
RUN pip install sliver-py
RUN git clone --depth 1 https://github.com/grpc/grpc
RUN cd grpc && git submodule update --init
RUN cd grpc && pip install -r requirements.txt
RUN cd grpc && pip uninstall protobuf
RUN cd grpc && pip install protobuf==3.20.*
RUN cd grpc && GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=True GRPC_PYTHON_BUILD_WITH_CYTHON=1 pip install .





