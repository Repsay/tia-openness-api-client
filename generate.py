import os
from typing import Any, Optional

import pandas as pd

from tia_portal import Client, DeviceItem


path_to_mock_data = os.path.join(os.path.dirname(__file__), 'mock_data.xlsx')

equipment = pd.read_excel(path_to_mock_data, dtype='object')
phases = pd.read_excel(path_to_mock_data, sheet_name='Phases')
phases = phases[phases['Phase 1'].notnull()]

sas = equipment["SA"].unique()
user_groups = {}

for sa in sas:
    sa_name = f"SA{sa}"
    user_groups[sa_name] = {"IDB": {}, "VDB": {}}
    user_groups[sa_name] = {key: {"IDB": {}, "VDB": {}} for key in equipment[equipment["SA"] == sa]["Station"].unique()}

function_blocks = {f"SA{sa}": {} for sa in sas}

for index, row in equipment.iterrows():
    sa_name = f"SA{row['SA']}"
    station = row['Station']
    fb_name = f"{row['Name']}_FB"
    if function_blocks[sa_name].get(station) is None:
        function_blocks[sa_name][station] = []

    if row['Name'] in phases['Equipment'].values:
        fb_seq_name = f"{row['Name']}_SEQ_FB"
        function_blocks[sa_name][station].append(fb_seq_name)

    function_blocks[sa_name][station].append(fb_name)

prodiag_blocks = {f"SA{sa}": {} for sa in sas}

for index, row in equipment.iterrows():
    sa_name = f"SA{row['SA']}"
    station = row['Station']
    fb_name = f"{sa_name}_EM{row['EM']}_PDIAG_FB"
    if prodiag_blocks[sa_name].get(station) is None:
        prodiag_blocks[sa_name][station] = []

    prodiag_blocks[sa_name][station].append(fb_name)
