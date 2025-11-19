# TIA Openness API Client - Usage Guide

This guide provides condensed documentation for common operations with the TIA Openness API Client. It covers how to access, create, and export PLCs, HMIs, blocks, and other hardware components.

## Table of Contents

- [Getting Started](#getting-started)
- [Project Operations](#project-operations)
- [Accessing Hardware](#accessing-hardware)
- [Creating Hardware](#creating-hardware)
- [Working with PLCs](#working-with-plcs)
- [Working with Blocks](#working-with-blocks)
- [Global Libraries](#global-libraries)
- [Complete Example](#complete-example)
- [Limitations](#limitations)
- [Additional Resources](#additional-resources)
- [Tips and Best Practices](#tips-and-best-practices)

## Getting Started

### Basic Setup

```python
import tia_portal.config as tia_config
from tia_portal import Client

# Load configuration
tia_config.load()

# Create a client instance
tia_client = Client()
```

## Project Operations

### Opening a Project

```python
# Open an existing project
project = tia_client.open_project(
    path="C:\\Users\\user\\Documents\\Automation",  # Path to Automation folder
    name="MyProject"  # Project name
)
```

### Creating a New Project

```python
# Create a new project
project = tia_client.create_project(
    path="C:\\Users\\user\\Documents\\Automation",
    name="NewProject"
)
```

### Saving a Project

```python
# Save the current project
project.save()

# Save as a new project
project.save_as("NewProjectName")
```

### Compiling a Project

```python
# Compile all software in the project
# This is required before exporting blocks
project.compile()
```

### Closing a Project

```python
# Close the project (saves automatically)
project.close()

# Force close without saving
project.force_close()
```

## Accessing Hardware

### Getting All Devices

```python
# Get all devices in the project
devices = project.devices

# Iterate through devices
for device in devices:
    print(f"Device: {device.name}")
```

### Getting Specific Device Items

```python
# Get all PLCs in the project
plcs = project.get_plcs()

for plc in plcs:
    print(f"PLC: {plc.name}")
```

### Accessing Device Items

```python
# Get a specific device item by name
device_item = project.get_device_item("PLC_1")

if device_item:
    print(f"Found device: {device_item.name}")
```

### Working with Device Hierarchy

```python
# Access devices and their items
for device in project.devices:
    print(f"Device: {device.name}")
    
    # Get items within this device
    device_items = device.get_items()
    for item in device_items:
        print(f"  Item: {item.name}")
        
        # Get nested items (if any)
        nested_items = item.get_items()
        if nested_items:
            for nested in nested_items:
                print(f"    Nested Item: {nested.name}")
```

## Creating Hardware

### Creating a PLC Device

```python
# Get the devices collection
devices = project.devices

# Create a PLC device
# You need the article number and version from TIA Portal
plc_device = devices.create_PLC(
    article_no="6ES7 511-1AK02-0AB0",  # Article number from TIA Portal
    version="V2.0",                     # Version
    name="PLC_1",                       # Network name
    device_name="PLC_1"                 # Device name in TIA Portal
)

print(f"Created PLC: {plc_device.name}")
```

### Creating an HMI Device

```python
# Create an HMI device
hmi_device = devices.create_HMI(
    article_no="6AV2 124-0MC01-0AX0",  # Article number from TIA Portal
    version="V15.1",                    # Version
    name="HMI_1"                        # Device name
)

print(f"Created HMI: {hmi_device.name}")
```

### Creating a Generic Device

For other device types, use the generic create method:

```python
# Create a device with hardware type identifier
device = devices.create(
    HwTypeIdentifier="OrderNumber:6ES7 515-2AM01-0AB0/V2.0",
    name="Device_1",
    device_name="MyDevice"
)
```

**Note:** To find the article number and version:
1. Open TIA Portal
2. Add a new device manually
3. The article number and version are shown in the device catalog

## Working with PLCs

### Accessing PLC Software

```python
# Get all PLCs
plcs = project.get_plcs()

if plcs:
    plc = plcs[0]  # Get the first PLC
    
    # Get the software of the PLC
    software = plc.get_software()
```

### Getting All Blocks

```python
# Get all blocks (non-recursive - only main block group)
blocks = software.get_all_blocks(recursive=False)

# Get all blocks recursively (includes system and user block groups)
all_blocks = software.get_all_blocks(recursive=True)

for block in all_blocks:
    print(f"Block: {block.name}")
```

### Accessing Specific Block Groups

```python
# Get main blocks
main_blocks = software.get_blocks()

# Get system block groups
system_groups = software.get_system_block_groups()

# Get user block groups
user_groups = software.get_user_block_groups()
```

### Working with Block Groups

```python
# Iterate through user block groups
user_groups = software.get_user_block_groups()
for group in user_groups:
    print(f"User Group: {group.name}")
    
    # Get blocks in this group
    blocks = group.get_blocks()
    for block in blocks:
        print(f"  Block: {block.name}")
    
    # Get nested groups
    nested_groups = group.get_groups()
    for nested in nested_groups:
        print(f"  Nested Group: {nested.name}")
```

## Working with Blocks

### Exporting Blocks

Blocks must be compiled before they can be exported.

```python
# Compile the project first
project.compile()

# Get all blocks
blocks = software.get_all_blocks(recursive=True)

# Export each block
for block in blocks:
    try:
        export_path = block.export()
        print(f"Exported {block.name} to {export_path}")
    except Exception as e:
        print(f"Failed to export {block.name}: {e}")
```

### Creating Blocks from XML

You can create blocks from XML files using the `create` method with custom labels for placeholder replacement.

```python
# Get the blocks collection
blocks = software.get_blocks()

# Create a block from an XML file
# The XML file should contain __NAME__ placeholder which will be replaced
new_block = blocks.create(
    path="C:\\path\\to\\block_template.xml",
    name="MyNewBlock",
    labels={
        "__NAME__": "MyNewBlock",
        "__CUSTOM_LABEL__": "CustomValue"  # Optional: additional replacements
    }
)

print(f"Created block: {new_block.name}")
```

**Note:** The XML file can contain placeholders like `__NAME__` which will be replaced with values from the `labels` dictionary. If `labels` is not provided, `__NAME__` will be replaced with the `name` parameter.

### Creating Instance Databases

Instance databases (DBs) are used with function blocks (FBs):

```python
# Get the blocks collection
blocks = software.get_blocks()

# Create an instance database linked to a function block
instance_db = blocks.create_instance_database(
    name="DB_MyInstance",
    fb_name="FB_MyFunctionBlock"  # The FB that this DB is an instance of
)

print(f"Created instance DB: {instance_db.name}")
```

### Creating ProDiag Blocks

ProDiag blocks are function blocks with automatic instance database creation:

```python
# Create a ProDiag function block
# This automatically creates the FB and its instance DB
prodiag_block = blocks.create_prodiag_block(name="FB_Diagnosis")

print(f"Created ProDiag block: {prodiag_block.name}")
# This also creates "IDB_Diagnosis" automatically in an "IDB" group
```

### Creating User Block Groups

```python
# Get user block groups collection
user_groups = software.get_user_block_groups()

# Create a new user block group
new_group = user_groups.create("MyBlockGroup")
print(f"Created group: {new_group.name}")

# You can then create blocks within this group
group_blocks = new_group.get_blocks()
```

### Getting Block Information

```python
# Get block type
block_type = block.get_type()
print(f"Block type: {block_type}")

# Check if block is consistent (compiled)
if block.value and block.value.IsConsistent:
    print("Block is compiled and consistent")
else:
    print("Block needs compilation")
```

## Global Libraries

### Accessing Global Libraries

```python
# Import GlobalLibraries class
from tia_portal import GlobalLibraries

# Get global libraries (requires a TIA Portal session)
libraries = GlobalLibraries(tia_client)

for library in libraries:
    print(f"Library: {library.name}")
```

### Finding a Specific Global Library

```python
# Find a specific global library by name
libraries = GlobalLibraries(tia_client)
library = libraries.find("MyLibrary")

if library.value is not None:
    print(f"Found library: {library.name}")
else:
    print("Library not found")
```

### Working with Library Types

```python
# Access library types through the type_folder property
types_folder = library.type_folder

# Get the types collection
types = types_folder.types

# Iterate through types
for lib_type in types:
    print(f"Library Type: {lib_type.name}")

# Access type folders (user-created folders)
type_folders = types_folder.folders
for folder in type_folders:
    print(f"Type Folder: {folder.name}")
```

### Working with Master Copies

```python
# Access master copies through the master_copy_folder property
master_copy_folder = library.master_copy_folder

# Get the master copies collection
master_copies = master_copy_folder.master_copies

# Iterate through master copies
for master_copy in master_copies:
    print(f"Master Copy: {master_copy.name}")

# Access master copy folders (user-created folders)
mc_folders = master_copy_folder.folders
for folder in mc_folders:
    print(f"Master Copy Folder: {folder.name}")
```

## Complete Example

Here's a complete example that demonstrates common operations:

```python
import tia_portal.config as tia_config
from tia_portal import Client

# Setup
tia_config.load()
tia_client = Client()

try:
    # Open a project
    project = tia_client.open_project(
        path="C:\\Users\\user\\Documents\\Automation",
        name="MyProject"
    )
    
    # Get PLCs
    plcs = project.get_plcs()
    
    if len(plcs) == 0:
        print("No PLCs found in project")
    else:
        plc = plcs[0]
        print(f"Working with PLC: {plc.name}")
        
        # Get software
        software = plc.get_software()
        
        # Get all blocks
        all_blocks = software.get_all_blocks(recursive=True)
        print(f"Found {len(all_blocks)} blocks")
        
        # Compile project
        print("Compiling project...")
        project.compile()
        print("Compilation complete")
        
        # Export all blocks
        for block in all_blocks:
            try:
                export_path = block.export()
                print(f"Exported: {block.name}")
            except Exception as e:
                print(f"Failed to export {block.name}: {e}")
        
        # Save project
        project.save()
        
finally:
    # Always close the client when done
    tia_client.close()
```

## Limitations

Based on the current implementation, please note:

1. **Import Functionality**: Direct import of complete hardware configurations or projects is not currently implemented. However, the library supports:
   - Creating blocks from XML templates
   - Exporting blocks to XML
   - Creating PLCs and HMIs via article numbers

2. **HMI Operations**: While HMI devices can be created and accessed through the device hierarchy, HMI-specific software operations (screens, tags, etc.) are limited. The library primarily focuses on PLC software operations.

3. **Hardware Identifiers**: When creating PLCs and HMIs, you need to know the exact article number and version from TIA Portal. These can be found in the hardware catalog when manually adding devices.

4. **Block Import**: Blocks can be created from XML files using templates with the `create()` method, but there is no direct "import from backup" method for blocks.

5. **Primary Use Case**: This library was primarily designed for:
   - Automating PLC code/block creation
   - Creating hardware devices (PLCs, HMIs)
   - Exporting blocks for backup or documentation
   - Managing project compilation and basic operations

For extending functionality beyond these capabilities, refer to the [Siemens TIA Openness Python Stubs](https://github.com/Repsay/siemens-tia-openness-python-stubs) repository for accessing the full TIA Openness API.

## Additional Resources

- **Repository**: [tia-openness-api-client](https://github.com/Repsay/tia-openness-api-client)
- **TIA Openness Stubs**: [siemens-tia-openness-python-stubs](https://github.com/Repsay/siemens-tia-openness-python-stubs)
- **Main Classes**:
  - `Client`: Main entry point for TIA Portal operations
  - `Project`: Project-level operations
  - `Device`: Hardware device representation
  - `DeviceItem`: Specific device items (PLCs, HMIs, etc.)
  - `PLCSoftware`: PLC software operations
  - `PLCBlock`: Individual block operations
  - `GlobalLibraries`: Access to global libraries
  - `GlobalLibrary`: Individual global library operations

## Tips and Best Practices

1. **Always compile before exporting**: Blocks must be compiled (consistent) before they can be exported.

2. **Use try-except blocks**: Many operations can fail if the TIA Portal state is inconsistent or files are missing.

3. **Close the client**: Always close the client when done to properly dispose of the TIA Portal session.

4. **Check for None values**: Many methods return `None` if objects don't exist. Always check before using.

5. **Recursive operations**: When getting blocks or groups, use the `recursive=True` parameter to get all nested items.

6. **Path separators**: Use double backslashes (`\\`) or raw strings (`r"C:\path"`) for Windows paths.

7. **Hardware article numbers**: To find article numbers for creating hardware, open TIA Portal's hardware catalog and note the article number and version of the device you want to create programmatically.

8. **Device naming**: When creating devices, be consistent with naming conventions. The `name` parameter is typically the network name, while `device_name` is the name shown in the TIA Portal project tree.
