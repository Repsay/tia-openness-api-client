# type: ignore
import tia_portal.config as tia_config
from tia_portal import Client

tia_config.load()

tia_client = Client()

tia_client.open_project("C:\\Users\\jdelahaije\\Documents\\Automation", "Generate")

plcs = tia_client.project.get_plcs()

if len(plcs) == 0:
    print("No PLCs found in project")
elif len(plcs) > 1:
    print("Multiple PLCs found in project")
else:
    plc = plcs[0]

    software = plc.get_software()

    if not software:
        # NOTE: This error is not emitted, because it is not possible to
        print("No software found in PLC")
        raise Exception("No software found in PLC")

    software_blocks = software.get_blocks()

    tia_client.project.compile()

    for block in software_blocks:
        try:
            block.export()
        except Exception as e:  # pylint: disable=broad-except
            print(e)
            continue


input("Press enter to continue...")
