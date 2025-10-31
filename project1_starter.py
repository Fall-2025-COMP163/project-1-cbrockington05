"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Cayden Brockington]
Date: [11/01/25]

AI Usage: ChatGPT helped me with function formatting and understanding the load_character logic
Example: AI helped with file I/O error handling logic in save_character function
"""

#character classes to choose from
given_classes = {'Warrior', 'Mage', 'Rogue', 'Cleric'}

def create_character(name, character_class):
   
    c = character_class.title()

    #starting character level and gold amount
    level = 1
    gold = 67

    #receives stats from calculate_stats function
    strength, magic, health = calculate_stats(c, level)
   
   #creating character dictionary
    character = {
        'name': name,
        'class': c,
        'level': level,
        'strength': strength,
        'magic': magic,
        'health': health,
        'gold': gold
    }

    return character
    
    
    
   
    # Remember to use calculate_stats() function for stat calculation
    
    


def calculate_stats(character_class, level):
    
    c = character_class.title()
    
    if c == 'Warrior':
        return 15 + (level -1) * 3, 5 + (level -1) *2, 120 + (level -1) *10
    
    elif c == 'Mage':
        return 5 + (level -1) *1, 15 + (level -1) *4, 80 + (level -1) *6

    elif c == 'Rogue':
        return 10 + (level -1) *2, 10 + (level -1) *2, 70 + (level -1) *5
    
    elif c == 'Cleric':
        return 10 + (level -1) *2, 15 + (level -1) *3, 110 + (level -1) *8
    
    else:
        print(f"Invalid class '{character_class}', defualting to Rogue.")
        return 10, 10, 70
    
    
   
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    

def save_character(character, filename):
    
    #open file in write mode
    with open(filename, 'w') as f:
        f.write(f'Character Name: {character["name"]}\n')
        f.write(f'Class: {character["class"]}\n')
        f.write(f'Level: {character["level"]}\n')
        f.write(f'Strength: {character["strength"]}\n')
        f.write(f'Magic: {character["magic"]}\n')
        f.write(f'Health: {character["health"]}\n')
        f.write(f'Gold: {character["gold"]}\n')

    
    
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    

def load_character(filename):
    
    import os

    #seeing if file exist
    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        return None

    character = {}

    #opening file and reading lines
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip() #get rid of whitespace
            if not line:
                continue #skipping any empty line
            
            #splitting at the first colon
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()

                #converting to integers
                if key in ['Level', 'Strength', 'Magic', 'Health', 'Gold']:
                    value = int(value)
                
                #convert the keys in file to dictionary keys
                if key == 'Character Name':
                    character['name'] = value
                
                elif key == 'Class':
                    character['class'] = value

                elif key == 'Level':
                    character['level'] = value

                elif key == 'Strength':
                    character['strength'] = value

                elif key == 'Magic':
                    character['magic'] = value

                elif key == 'Health':
                    character['health'] = value

                elif key == 'Gold':
                    character['gold'] = value

    return character
                

   
    # TODO: Implement this function
    # Remember to handle file not found errors
    

def display_character(character):
    
    #print character info
    print('=== CHARACTER SHEET ===')
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")


    
    # TODO: Implement this function
    

def level_up(character):
    
    #increasing level by 1
    character['level'] += 1

    #recalculating stats after level up
    strength, magic, health = calculate_stats(character['class'], character['level'])
    character['strength'] = strength
    character['magic'] = magic
    character['health'] = health
    
   

   
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    

# Main program area (optional - for testing your functions)
#if __name__ == "__main__":
    #print("=== CHARACTER CREATOR ===")
    #print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
