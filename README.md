# slithic
Using Mythic C2 to control / integrate Sliver C2

- assumes sliver with default install on ubuntu 22 vm
- assumes mthic install on same ubuntu 22 vm

## TODOs

- [x] ubuntu 22 VM installed
    - [x] running sliver with defaults
- [x] ubuntu 22 container
    - [x] sliver-py installed (1.6x version?)
    - [x] connect.py ready
    - [x] mythic.cfg ready (transfer from VM)
    - [x] able to connect!
- [x] Mythic install
    - [x] jupyter notebook can connect to sliver!
    - [ ] start creation of mythic things

## Next Steps

- Mythic installed on ubuntu 22 VM
- Jupyter notebook to install sliver-py with version 1.6?
- connect to the localhost sliver

- Mythic development flow started
    - ubuntu 22 container however mythic needs it
    - 'build a payload'
    - something to keep updated / synced with sliver
    - ??? tasking via mythic?
    - interactive sessions as stretch goal

### Required fixes

// run within venv if you want?
sudo apt-get install build-essential python3-dev libssl-dev
pip install sliver-py
git clone https://github.com/grpc/grpc
cd grpc
git submodule update --init
pip install -r requirements.txt
pip uninstall protobuf
pip install protobuf==3.20.*
GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=True GRPC_PYTHON_BUILD_WITH_CYTHON=1 pip install .

### what are we doing right now

- installed mythic (good)
- docker exec -it --user root mythic_jupyter /bin/bash
    - apt-get updates and install and process for sliver-py fix

- TODO: devcontainer that already has this setup? (use as base for mythic container things...)
    - experiment with rebuilding the devcontainer... (cause rebuilding grpc takes a while...)





