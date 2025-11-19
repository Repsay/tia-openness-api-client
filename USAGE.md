# TIA Openness API Client - Usage Guide

This guide provides condensed documentation for common operations with the TIA Openness API Client.

## Table of Contents

- [Getting Started](#getting-started)
- [Project Operations](#project-operations)
- [Accessing Hardware](#accessing-hardware)
- [Working with PLCs](#working-with-plcs)
- [Working with Blocks](#working-with-blocks)
- [Global Libraries](#global-libraries)
- [Limitations](#limitations)

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

### Creating User Block Groups

```python
# Get user block groups collection
user_groups = software.get_user_block_groups()

# Create a new user block group
new_group = user_groups.create("MyBlockGroup")
print(f"Created group: {new_group.name}")
```

## Global Libraries

### Accessing Global Libraries

```python
# Get global libraries (requires an open project)
libraries = tia_client.get_global_libraries()

for library in libraries:
    print(f"Library: {library.name}")
```

### Opening a Global Library

```python
# Open a specific global library
library = tia_client.open_global_library(
    path="C:\\path\\to\\libraries",
    name="MyLibrary"
)
```

### Working with Library Types

```python
# Access library types
types_folder = library.get_types()

# Get all types recursively
all_types = types_folder.get_all_types(recursive=True)

for lib_type in all_types:
    print(f"Library Type: {lib_type.name}")
```

### Working with Master Copies

```python
# Access master copies
master_copies_folder = library.get_master_copies()

# Get all master copies recursively
all_master_copies = master_copies_folder.get_all_master_copies(recursive=True)

for master_copy in all_master_copies:
    print(f"Master Copy: {master_copy.name}")
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

1. **Import Functionality**: Direct import of PLCs, HMIs, or complete hardware configurations is not currently implemented in this library. The library primarily supports:
   - Creating blocks from XML templates
   - Exporting blocks to XML

2. **Hardware Creation**: Direct creation of new hardware devices (PLCs, HMIs) is not currently implemented. The library is designed to work with existing devices in projects.

3. **HMI Operations**: While HMI devices can be accessed through the device hierarchy, HMI-specific operations are limited. The library primarily focuses on PLC software operations.

4. **Block Import**: Blocks can be created from XML files using templates with the `create()` method, but there is no direct "import" method for blocks.

5. **Primary Use Case**: This library was primarily designed for:
   - Automating PLC code/block creation
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
  - `GlobalLibrary`: Global library operations

## Tips and Best Practices

1. **Always compile before exporting**: Blocks must be compiled (consistent) before they can be exported.

2. **Use try-except blocks**: Many operations can fail if the TIA Portal state is inconsistent or files are missing.

3. **Close the client**: Always close the client when done to properly dispose of the TIA Portal session.

4. **Check for None values**: Many methods return `None` if objects don't exist. Always check before using.

5. **Recursive operations**: When getting blocks or groups, use the `recursive=True` parameter to get all nested items.

6. **Path separators**: Use double backslashes (`\\`) or raw strings (`r"C:\path"`) for Windows paths.
