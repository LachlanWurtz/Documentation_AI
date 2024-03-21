# import dependencies 
from docxtpl import DocxTemplate

from create_document import create_document

# Define template data
template_data = {
    'product_name': 'default name',
    'introduction': 'Introduction goes here',
    'specifications': 'Specifications go here',
    'intended_use': 'Intended Use goes here',
    'audience': 'Audience information goes here',
    'setup': 'Setup instructions go here',
    'usage_guidelines': 'Usage guidelines go here',
    'maintenance': 'Maintenance procedures go here',
    'troubleshooting': 'Troubleshooting section goes here',
    'safety': 'Safety information goes here',
    'environmental': 'Environmental considerations go here',
    'regulatory_standards': 'Compliance with regulatory standards goes here'
}

#main function
def main():    
    create_document(template_data)


main()