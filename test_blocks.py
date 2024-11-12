from barfi import Block

# Define the Curriculum block (Input Block)
curriculum = Block(name='Curriculum')
# Remove the output port by commenting out or deleting the add_output() line
# curriculum.add_output()
# The 'name' parameter is 'Type here...' to display as placeholder text
curriculum.add_option(name='Type here...', type='input', value='')

def curriculum_compute(self):
    # Get the user's input using the new option name
    value = self.get_option('Type here...')
    # Since there is no output interface, we don't need to set it
    pass  # No further action needed

curriculum.add_compute(curriculum_compute)

# Define the Topic block
topic = Block(name='Topic')
# **Add an output port to match 'Sub-Topic'**
topic.add_output()
topic.add_option(name='Type here...', type='input', value='')

def topic_compute(self):
    value = self.get_option('Type here...')
    # **Set the output interface value to match 'Sub-Topic'**
    self.set_interface(name='Output 1', value=value)

topic.add_compute(topic_compute)

# Define the Sub-Topic block
sub_topic = Block(name='Sub-Topic')
# **Add an input port to match 'Concept'**
sub_topic.add_input()
sub_topic.add_output()
sub_topic.add_option(name='Type here...', type='input', value='')

def sub_topic_compute(self):
    # **Get the value from the input interface to match 'Concept'**
    in_value = self.get_interface(name='Input 1')
    value = self.get_option('Type here...')
    # **Optionally, you might combine 'in_value' and 'value' if needed**
    # For now, we'll pass 'value' to the output interface
    self.set_interface(name='Output 1', value=value)

sub_topic.add_compute(sub_topic_compute)

# Define the Concept block (Result Block)
concept = Block(name='Concept')
concept.add_input()
concept.add_option(name='Type here...', type='input', value='')

def concept_compute(self):
    # Get the value from the input interface
    in_value = self.get_interface(name='Input 1')
    # Get the value from the input option
    input_value = self.get_option('Type here...')
    # Process or store these values as needed
    pass  # Replace with your logic here

concept.add_compute(concept_compute)

# Define the base blocks list and category
base_blocks = [curriculum, topic, sub_topic, concept]
base_blocks_category = {
    'Multiple': [sub_topic, concept, topic],
    'One Per Category': [curriculum],
}