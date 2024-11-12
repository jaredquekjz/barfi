from matplotlib import pyplot as plt
from barfi import st_barfi, barfi_schemas
import streamlit as st
from test_blocks import base_blocks, base_blocks_category
import pandas as pd  # Import pandas for DataFrame
import json  # Import json to parse JSON strings

st.set_page_config(layout="wide")

def colorful_title(text):
    colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FF33F3', '#FF33F3', '#33FFF3', '#F3FF33']
    colored_text = ''
    color_index = 0
    for char in text:
        if char != ' ':
            colored_text += f'<span style="color:{colors[color_index % len(colors)]};">{char}</span>'
            color_index += 1
        else:
            colored_text += ' '  # Preserve spaces
    return f'<h1 style="text-align: center;">{colored_text}</h1>'

# Display the colorful title
st.markdown(colorful_title('Fun Blocks Content Map'), unsafe_allow_html=True)

barfi_schema_name = st.selectbox(
    'Select a saved content map:', barfi_schemas()
)


# Add line break before
st.markdown("<br>", unsafe_allow_html=True)

# Add the centered, italicized information message in a light blue box using Streamlit's default font
st.write(
    "<div style='text-align: center; font-style: italic; background-color: rgba(28, 131, 225, 0.1); padding: 15px; border-radius: 5px; border: 1px solid rgba(28, 131, 225, 0.2); color: #fff;'>ℹ️ The relative numbering of your blocks indicate the order in which your inputs will appear in the CSV file. They need not be in exact sequence. For example, Concept-1, Concept-3, Concept-5 will appear in that sequence for the same Sub-Topic.</div>", 
    unsafe_allow_html=True
)

# Add line break after
st.markdown("<br>", unsafe_allow_html=True)

# Remove the compute engine checkbox and set compute_engine to False
compute_engine = False

# Initialize an empty DataFrame
df = pd.DataFrame()

barfi_result = st_barfi(
    base_blocks=base_blocks_category,
    compute_engine=compute_engine,
    load_schema=barfi_schema_name,
)

def extract_input_values(barfi_result):
    import json
    import pandas as pd
    import streamlit as st

    # Parse barfi_result
    if isinstance(barfi_result, dict):
        barfi_output = barfi_result
    else:
        # barfi_result is a string, attempt to parse it
        try:
            barfi_output = barfi_result
            # Keep parsing as long as barfi_output is a string
            while isinstance(barfi_output, str):
                barfi_output = json.loads(barfi_output)
        except (TypeError, json.JSONDecodeError) as e:
            st.error(f"Failed to parse barfi_result as JSON. Error: {e}")
            st.write("barfi_result:", barfi_result)
            st.write("repr(barfi_result):", repr(barfi_result))
            return

    # Extract nodes and connections
    nodes = barfi_output.get('editor_state', {}).get('nodes', [])
    connections = barfi_output.get('editor_state', {}).get('connections', [])

    # Map node IDs to their info
    node_id_to_info = {}
    for node in nodes:
        options_dict = {key: value for key, value in node.get('options', [])}
        node_id_to_info[node['id']] = {
            'id': node['id'],
            'name': node['name'],
            'type': node['type'],
            'options': options_dict,
            'interfaces': {
                interface[1]['id']: {
                    'name': interface[0],
                    'value': interface[1].get('value'),
                    'node_id': node['id']
                }
                for interface in node.get('interfaces', [])
            }
        }

    # Collect Level 1 (Curriculum)
    level1_value = ''
    for node_id, info in node_id_to_info.items():
        if info['type'] == 'Curriculum':
            level1_value = info['options'].get('Type here...', '').strip()
            break  # Assuming only one Curriculum node

    # Collect Level 2 nodes (Topics)
    level2_nodes = {}
    for node_id, info in node_id_to_info.items():
        if info['type'] == 'Topic':
            level2_value = info['options'].get('Type here...', '').strip()
            if level2_value != '':
                output_interfaces_ids = [
                    iface_id for iface_id in info['interfaces']
                    if info['interfaces'][iface_id]['name'].startswith('Output')
                ]
                level2_nodes[node_id] = {
                    'id': node_id,
                    'value': level2_value,
                    'output_interfaces_ids': output_interfaces_ids
                }

    # Collect Level 3 nodes (Sub-Topics)
    level3_nodes = {}
    for node_id, info in node_id_to_info.items():
        if info['type'] == 'Sub-Topic':
            level3_value = info['options'].get('Type here...', '').strip()
            if level3_value != '':
                input_interfaces_ids = [
                    iface_id for iface_id in info['interfaces']
                    if info['interfaces'][iface_id]['name'].startswith('Input')
                ]
                output_interfaces_ids = [
                    iface_id for iface_id in info['interfaces']
                    if info['interfaces'][iface_id]['name'].startswith('Output')
                ]
                level3_nodes[node_id] = {
                    'id': node_id,
                    'value': level3_value,
                    'input_interfaces_ids': input_interfaces_ids,
                    'output_interfaces_ids': output_interfaces_ids
                }

    # Collect Level 4 nodes (Concepts)
    level4_nodes = {}
    for node_id, info in node_id_to_info.items():
        if info['type'] == 'Concept':
            level4_value = info['options'].get('Type here...', '').strip()
            if level4_value != '':
                input_interfaces_ids = [
                    iface_id for iface_id in info['interfaces']
                    if info['interfaces'][iface_id]['name'].startswith('Input')
                ]
                level4_nodes[node_id] = {
                    'id': node_id,
                    'value': level4_value,
                    'input_interfaces_ids': input_interfaces_ids
                }

    # Build mapping from Level 2 to Level 3
    level2_to_level3 = {level2_info['value']: [] for level2_info in level2_nodes.values()}

    for connection in connections:
        from_interface_id = connection['from']
        to_interface_id = connection['to']

        # Find Level 2 associated with from_interface_id
        for level2_id, level2_info in level2_nodes.items():
            if from_interface_id in level2_info['output_interfaces_ids']:
                level2_value = level2_info['value']

                # Find Level 3 associated with to_interface_id
                for level3_id, level3_info in level3_nodes.items():
                    if to_interface_id in level3_info['input_interfaces_ids']:
                        level3_value = level3_info['value']

                        if level3_value not in level2_to_level3[level2_value]:
                            level2_to_level3[level2_value].append(level3_value)

    # Build mapping from Level 3 to Level 4
    level3_to_level4 = {level3_info['value']: [] for level3_info in level3_nodes.values()}

    for connection in connections:
        from_interface_id = connection['from']
        to_interface_id = connection['to']

        # Find Level 3 associated with from_interface_id
        for level3_id, level3_info in level3_nodes.items():
            if from_interface_id in level3_info['output_interfaces_ids']:
                level3_value = level3_info['value']

                # Find Level 4 associated with to_interface_id
                for level4_id, level4_info in level4_nodes.items():
                    if to_interface_id in level4_info['input_interfaces_ids']:
                        level4_value = level4_info['value']

                        if level4_value not in level3_to_level4[level3_value]:
                            level3_to_level4[level3_value].append(level4_value)

    # Build DataFrame data
    data_list = []
    for idx, (level2_value, level3_list) in enumerate(level2_to_level3.items()):
        # Only add the Level 1 and Level 2 row if it's the first Topic
        if idx == 0:
            data_list.append({
                'Type': '',  # Or 'Topic' if you prefer
                'Level 1': level1_value,
                'Level 2': level2_value,
                'Level 3': '',
                'Level 4': ''
            })
        else:
            # For additional Topics, only add Level 2
            data_list.append({
                'Type': '',
                'Level 1': '',
                'Level 2': level2_value,
                'Level 3': '',
                'Level 4': ''
            })

        for level3_value in level3_list:
            # Add Level 3 Sub-Topic row
            data_list.append({
                'Type': 'Node',
                'Level 1': '',
                'Level 2': '',
                'Level 3': f"<span style='color: orange;'>{level3_value}</span>",
                'Level 4': ''
            })

            # Add Level 4 items under the Level 3 in Level 3 column
            level4_list = level3_to_level4.get(level3_value, [])
            if level4_list:
                for level4_value in level4_list:
                    data_list.append({
                        'Type': 'LO',
                        'Level 1': '',
                        'Level 2': '',
                        'Level 3': level4_value,  # Level 4 value shown in Level 3 column
                        'Level 4': ''  # Keep Level 4 column empty
                    })
            else:
                # Optionally, include a message if there are no Level 4 items
                pass

    # Create DataFrame
    df = pd.DataFrame(data_list)

    # Reorder columns to ensure all expected columns are present
    columns_order = ['Type', 'Level 1', 'Level 2', 'Level 3', 'Level 4']
    df = df.reindex(columns=columns_order)

    # Convert all columns to string, replace NaN with empty string
    df = df.fillna('').astype(str)

    # --- Shift 'Type' and 'Level 3' Columns Up ---
    df['Type'] = df['Type'].shift(-1)
    df['Level 3'] = df['Level 3'].shift(-1)

    # Remove the last row since 'Type' and 'Level 3' will have NaN after shifting
    df = df[:-1]
    # --- End of Shift ---

    # Remove "Type" from the heading of the first column
    df.rename(columns={'Type': ''}, inplace=True)

    # Remove any rows where all Level columns are empty (to remove empty rows)
    df = df[(df[['Level 1', 'Level 2', 'Level 3', 'Level 4']] != '').any(axis=1)]

    # Adjust DataFrame styles for alignment and display
    df_style = df.style.set_properties(**{'text-align': 'left'}).hide_index()

    # Render the DataFrame with HTML formatting
    st.write(df_style.to_html(index=False, escape=False), unsafe_allow_html=True)

    # Add a spaced line break between the DataFrame and the download button
    st.markdown('<br>', unsafe_allow_html=True)

    # Include the download button after DataFrame is populated
    if not df.empty:
        # Create a clean DataFrame for CSV export by removing HTML tags
        df_csv = df.copy()
        df_csv['Level 3'] = df_csv['Level 3'].str.replace(r'<[^>]*>', '', regex=True)

        # Remove "Type" from the heading of the first column in CSV
        df_csv.rename(columns={'Type': ''}, inplace=True)

        # Convert DataFrame to CSV
        csv = df_csv.to_csv(index=False).encode('utf-8')

        # Construct the file name using the Level 1 value
        file_name = f"{level1_value} Content Map.csv"

        st.download_button(
            label='Download Data as CSV',
            data=csv,
            file_name=file_name,
            mime='text/csv',
        )

if barfi_result:
    extract_input_values(barfi_result)