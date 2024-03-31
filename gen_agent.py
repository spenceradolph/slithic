import asyncio
from sliver import SliverClientConfig, SliverClient, client_pb2

CONFIG_PATH = "/workspaces/slithic/mythic.cfg"

async def main():
    config = SliverClientConfig.parse_config_file(CONFIG_PATH)
    client = SliverClient(config)
    await client.connect()

    implant_config = client_pb2.ImplantConfig(
        IsBeacon=True,
        Name="sliver-pytest-1",
        GOARCH="amd64",
        GOOS="linux",
        Format=client_pb2.OutputFormat.EXECUTABLE,
        ObfuscateSymbols=False,
        C2=[client_pb2.ImplantC2(Priority=0, URL="http://localhost:80")],
    )

    implant = await client.generate_implant(implant_config)

    f = open("implant_test_exe", "wb")
    f.write(implant.File.Data)
    f.close()


if __name__ == '__main__':
    asyncio.run(main())
