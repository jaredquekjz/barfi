from barfi import Block

# Define the Curriculum block (Input Block)
curriculum = Block(name='Curriculum')
curriculum.add_output()
# Set the 'value' parameter to an empty string to remove the placeholder
curriculum.add_option(name='input-option', type='input', value='')

def curriculum_compute(self):
    # Set the output interface value to the input option value
    value = self.get_option('input-option')
    self.set_interface(name='Output 1', value=value)

curriculum.add_compute(curriculum_compute)

# Define the Topic block (Input Block)
topic = Block(name='Topic')
topic.add_output()
# Set the 'value' parameter to an empty string
topic.add_option(name='input-option', type='input', value='')

def topic_compute(self):
    # Set the output interface value to the input option value
    value = self.get_option('input-option')
    self.set_interface(name='Output 1', value=value)

topic.add_compute(topic_compute)

# Define the Sub-Topic block (Input Block)
sub_topic = Block(name='Sub-Topic')
sub_topic.add_output()
# Set the 'value' parameter to an empty string
sub_topic.add_option(name='input-option', type='input', value='')

def sub_topic_compute(self):
    # Set the output interface value to the input option value
    value = self.get_option('input-option')
    self.set_interface(name='Output 1', value=value)

sub_topic.add_compute(sub_topic_compute)

# Define the Concept block (Result Block)
concept = Block(name='Concept')
concept.add_input()
# Set the 'value' parameter to an empty string
concept.add_option(name='input-option', type='input', value='')

def concept_compute(self):
    # Get the value from the input interface
    in_value = self.get_interface(name='Input 1')
    # Get the value from the input option
    input_value = self.get_option('input-option')
    # Process or store these values as needed
    pass  # Replace with your logic here

concept.add_compute(concept_compute)

# Define the base blocks list and category
base_blocks = [curriculum, topic, sub_topic, concept]
base_blocks_category = {
    'Inputs': [curriculum, topic, sub_topic],
    'Result': [concept]
}