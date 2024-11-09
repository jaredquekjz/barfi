import sys
sys.path.append('../')
from matplotlib import pyplot as plt
from barfi import st_barfi, barfi_schemas
import streamlit as st
from test_blocks import base_blocks, base_blocks_category
import pandas as pd  # Import pandas for DataFrame
import json  # Import json to parse JSON strings


def colorful_title(text):
    colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FF33F3', '#33FFF3', '#F3FF33']
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
    'Select a saved schema to load:', barfi_schemas()
)

compute_engine = st.checkbox('Activate barfi compute engine', value=False)

# Initialize an empty DataFrame
df = pd.DataFrame()

# Include the download button at the top of the app
if not df.empty:
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label='Download Data as CSV',
        data=csv,
        file_name='barfi_data.csv',
        mime='text/csv',
    )

barfi_result = st_barfi(
    base_blocks=base_blocks_category,
    compute_engine=compute_engine,
    load_schema=barfi_schema_name,
)

def extract_input_values(barfi_result):
    global df
    # Check the type of barfi_result
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

    # Now, barfi_output should be a dictionary
    nodes = barfi_output.get('editor_state', {}).get('nodes', [])
    connections = barfi_output.get('editor_state', {}).get('connections', [])

    # Map node IDs to their info
    node_id_to_info = {}
    for node in nodes:
        node_id_to_info[node['id']] = {
            'id': node['id'],
            'name': node['name'],
            'type': node['type'],
            'options': {key: value for key, value in node.get('options', [])},
            'interfaces': {
                interface[1]['id']: {
                    'name': interface[0],
                    'value': interface[1].get('value'),
                    'node_id': node['id']
                }
                for interface in node.get('interfaces', [])
            }
        }

    # Map interface IDs to node IDs
    interface_id_to_node_id = {}
    for node in nodes:
        for interface in node.get('interfaces', []):
            interface_id = interface[1]['id']
            interface_id_to_node_id[interface_id] = node['id']

    # Initialize data list to collect rows for the DataFrame
    data_list = []

    # Collect Curriculum and Topic values regardless of connections
    curriculum_values = []
    topic_values = []

    for node_id, info in node_id_to_info.items():
        if info['type'] == 'Curriculum':
            curriculum_value = info['options'].get('input-option', '')
            curriculum_values.append(curriculum_value)
        elif info['type'] == 'Topic':
            topic_value = info['options'].get('input-option', '')
            topic_values.append(topic_value)

    # Use the first Curriculum and Topic values (assuming one each)
    curriculum_value = curriculum_values[0] if curriculum_values else ''
    topic_value = topic_values[0] if topic_values else ''

    # Identify all Sub-Topic output interfaces
    sub_topic_output_interfaces = {}
    for node in nodes:
        if node['type'] == 'Sub-Topic':
            sub_topic_interfaces = node.get('interfaces', [])
            for interface in sub_topic_interfaces:
                if interface[0].startswith('Output'):
                    sub_topic_output_interfaces[interface[1]['id']] = node['id']

    # Identify all Concept input interfaces
    concept_input_interfaces = {}
    for node in nodes:
        if node['type'] == 'Concept':
            concept_interfaces = node.get('interfaces', [])
            for interface in concept_interfaces:
                if interface[0].startswith('Input'):
                    concept_input_interfaces[interface[1]['id']] = node['id']

    # Find all connections between Sub-Topic outputs and Concept inputs
    found_connections = False
    for connection in connections:
        from_interface_id = connection['from']
        to_interface_id = connection['to']

        if (from_interface_id in sub_topic_output_interfaces and
            to_interface_id in concept_input_interfaces):

            sub_topic_node_id = sub_topic_output_interfaces[from_interface_id]
            concept_node_id = concept_input_interfaces[to_interface_id]

            # Collect values for each connection
            sub_topic_value = node_id_to_info[sub_topic_node_id]['options'].get('input-option', '')
            concept_value = node_id_to_info[concept_node_id]['options'].get('input-option', '')

            # Create a data dictionary for this row
            data = {
                'Curriculum': curriculum_value if not found_connections else '',
                'Topic': topic_value if not found_connections else '',
                'Sub-Topic': sub_topic_value,
                'Concept': concept_value
            }

            # After the first row, set Curriculum and Topic to empty strings
            found_connections = True

            # Add the data dictionary to the data list
            data_list.append(data)

    # If data_list is not empty, create the DataFrame
    if data_list:
        df = pd.DataFrame(data_list)
    else:
        # Show Curriculum and Topic even if there are no Sub-Topic to Concept connections
        data = {
            'Curriculum': curriculum_value,
            'Topic': topic_value
        }
        df = pd.DataFrame([data])

    # Convert all columns to string to ensure correct alignment
    df = df.astype(str)

    # Display the DataFrame without the index and left-aligned
    st.write(df.to_html(index=False, justify='left'), unsafe_allow_html=True)

    # Display the JSON output for debugging
    st.write("barfi_result JSON output:")
    st.write(barfi_result)

if barfi_result:
    extract_input_values(barfi_result)
    # Include the download button after DataFrame is populated
    if not df.empty:
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label='Download Data as CSV',
            data=csv,
            file_name='barfi_data.csv',
            mime='text/csv',
        )