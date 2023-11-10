import re

def get_celebrity_info(celebrity_name, celebrity_data):
    match = None
    for entry in celebrity_data:
        if celebrity_name.lower() in entry['name'].lower():
            match = entry
            break

    if match:
        # Extract information using regular expressions
             
        occupation = re.search(r'(?i)occupation:\s*(\S+)', match['info'])
        age = re.search(r'(?i)age:\s*(\S+)', match['info'])
        nationality = re.search(r'(?i)nationality:\s*(\S+)', match['info'])

        # Print the extracted information
       
        print(f'Occupation: {occupation.group(1) if occupation else "Format not found"}')
        print(f'Age: {age.group(1) if age else "Format not found"}')
        print(f'Nationality: {nationality.group(1) if nationality else "Format not found"}')
    else:
        print(f'Unable to fetch information!')

# Example usage:
celebrity_data = [
   {'name': 'Elon Musk', 'info': 'Date of Birth: June 28, 1971\nOccupation: Entrepreneur\nAge: 52\nNationality: American'},
    {'name': 'Taylor Swift', 'info': 'Date of Birth: December 13, 1989\nOccupation: Singer\nAge: 32\nNationality: American'},
    # Add more celebrity data as needed
]

def main():
     print("Hi!, I am your talkbot\n")
     while True:
         user_input = input("Which celebrity information you need?, or type 'quit' to exit: ")
         if user_input.lower() == 'quit':
             print("Thank you, visit again")
             break
             
         else:
             celebrity_name = user_input
             print((user_input),"'s information")
             info =  get_celebrity_info(celebrity_name, celebrity_data)
             
if __name__ == "__main__":
    main()