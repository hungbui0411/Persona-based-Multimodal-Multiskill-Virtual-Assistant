from persona_core import PersonaCore
from persona_specs import PersonaSpecs
import logging
import argparse

def add_logger():
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(handler_format)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return logger

def process_persona(persona_directory):
    path = f"/Users/hungbui/Desktop/Persona AI/python-persona-bot/data/characters/{persona_directory}"

    name = None
    greeting = None
    short_description = None
    long_description = None
    character_categories = None
    persona_definition = None
    user_name = None

    # Path for those variables
    name_path = f"{path}/name.txt"
    greeting_path = f"{path}/greeting.txt"
    short_description_path = f"{path}/short_description.txt"
    long_description_path = f"{path}/long_description.txt"
    character_categories_path = f"{path}/character_categories.txt"
    persona_definition_path = f"{path}/persona_definition.txt"
    user_name_path = f"{path}/user_name.txt"

    #print("=====TYPES OF THE ATTRIBUTES IN PERSONA SPECS=====")
    # Let's shorten this later, after we have completed other more essential functions
    with open(name_path, 'r') as reader:
        name = reader.read()
        #print(f"name: {type(name)}")
    with open(greeting_path, 'r') as reader:
        greeting = reader.read()
        #print(f"greeting: {type(greeting)}")
    with open(short_description_path, 'r') as reader:
        short_description = reader.read()
        #print(f"short_description: {type(short_description)}")
    with open(long_description_path, 'r') as reader:
        long_description = reader.read()
        #print(f"long_description: {type(long_description)}")
    with open(character_categories_path, 'r') as reader:
        character_categories = reader.read()
        #print(f"character_categories: {type(character_categories)}")
    with open(persona_definition_path, 'r') as reader:
        persona_definition = reader.read()
        #print(f"persona_definition: {type(persona_definition)}")
    with open(user_name_path, 'r') as reader:
        user_name = reader.read()
        #print(f"user_name: {type(user_name)}")

    persona_specs = PersonaSpecs(
        name=name,
        greeting=greeting,
        short_description=short_description,
        long_description=long_description,
        character_categories=character_categories,
        persona_definition=persona_definition,
        user_name=user_name)

    #persona_specs.print()

    return persona_specs

def main():
    """
    Handles the flow of the assistant
    :return:
    """
    parser = argparse.ArgumentParser(
        description = "Persona Core Activation Point"
    )

    parser.add_argument(
        "persona_directory",
        help="Location of the character directory with the following files: name, greeting, short_description, long_description, character_categories, persona_definition, user_name"
    )

    args = parser.parse_args()
    persona_directory = args.persona_directory

    # Persona Directory is currently just the name of the character
    persona_specs = process_persona(persona_directory)

    logger = add_logger()
    logger.info("---Activating Persona.AI---")
    core = PersonaCore(persona_specs)
    core.run()

if __name__ == '__main__':
    main()