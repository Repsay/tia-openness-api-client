# tia-openness-api-client

`tia-openness-api-client` is a Python library used to create a client for accessing the TIA Openness API in Python. With this library, you can interact with TIA Portal and perform various tasks programmatically, such as creating and modifying project files, exporting and importing data, and much more.

## TIA Openness API

The TIA Openness API is a powerful tool for automating tasks in TIA Portal, Siemens' engineering framework for automation projects. Using the API, you can develop custom software that interacts with TIA Portal, allowing you to automate repetitive tasks, streamline workflows, and improve productivity.

The API provides access to all the features of TIA Portal, including creating and modifying project files, adding and configuring devices, configuring network settings, and much more. With the TIA Openness API, you can automate complex engineering tasks and accelerate your development processes.

## Usage

Here's an example of how to use tia-openness-api-client to create a new project in TIA Portal:

```python
import tia_portal.config as tia_config
from tia_portal import Client

tia_config.load()

tia_client = Client()

tia_client.open_project("C:\\Users\\user\\Documents\\Automation", "NAME")

tia_client.project.save_as("NAME_2")

plcs = tia_client.project.get_plcs()

if len(plcs) == 0:
    print("No PLCs found in project")
elif len(plcs) > 1:
    print("Multiple PLCs found in project")
else:
    plc = plcs[0]

    software = plc.get_software()

    software_blocks = software.get_all_blocks(True)

    print("Compiling project...", end="\r")
    tia_client.project.compile()
    print("Compiling project... Done")

    for block in software_blocks:
        print(block.name, end="\r")
        try:
            block.export()
        except Exception as e:
            print(e)
            continue

input("Press Enter to continue...")
```

The example code above uses the tia_portal library to open a project in TIA Portal located at "C:\Users\user\Documents\Automation" with project name "NAME", saves it as a new project with name "NAME_2", and then exports all the software blocks from the project.

Please note that some lines of code have been commented out and are not being executed, and that the input() call at the end is used to keep the console window open until the user presses Enter.

## Installation

To install tia-openness-api-client, you can use pip:

```bash
pip install -e .
```

This will install the tia_portal library as an editable package, allowing you to make changes to the source code and have them reflected in your Python environment.

This repository is developed using Python 3.11, but with some modifications, it may be possible to make it compatible with older versions of Python. However, since I cannot test the code myself due to the unavailability of TIA Portal and TIA Openness, I cannot guarantee full compatibility or provide specific instructions for adapting the code to older Python versions. If you choose to make it compatible with an older version, it is advisable to review the code carefully, resolve any potential syntax or module compatibility issues, and thoroughly test the modified code to ensure its proper functioning.

Additionally, if you are able to make the necessary changes to make this repository compatible with older versions of Python, I encourage you to contribute your modifications back to the project. By doing so, you can help other users who may be in a similar situation and ensure the codebase remains accessible and useful to a wider audience. Sharing your updates, bug fixes, or compatibility improvements with the community is a valuable contribution that can benefit the entire development community.

## Contributing

If you'd like to contribute to tia-openness-api-client, please fork the repository and create a new branch for your changes. Once you've made your changes, submit a pull request and we'll review your changes.

## License

tia-openness-api-client is licensed under the MIT License. See LICENSE for more information.
