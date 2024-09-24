# dictionaries.py

from platform import java_ver
from traceback import print_tb


def demo():
    """
    Demonstrate basic disctionary stuff
    """
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)
    
    # Iterate over the dictionary by key
    for key in myDictionary.keys():
        print(key)
        
    # Iterate by value/key
    for item in myDictionary.items():
        print(item)
        
    # Iterate by value
    for value in myDictionary.values():
        print(value)
        
    # Add a key/value pair to the dictionary
    myDictionary["Michigan State"] = "Spartans"
    
    print(len(myDictionary))
    
    #Cause an exception. Add try / except logic to handle this
    try:
        print(myDictionary["Ohio State"])
    except :
        # We end up here if an exception is thrown in the try block
        print("GOOD TRY")
    
    # Remove Xavier by key abd print the dictionary
    myDictionary.pop("Xavier")
    print(myDictionary)
    
    # Create another dictionary called newTEams
    # Add several key/value pairs
    # Combine that with myDictionary and print the results
    newTeams = {"Porto Alegre":"Internacional", "Goiania":"Goias", "Brasilia":"Gama", "Recife":"Sport"}
    """
    for key in newTeams.keys()
        myDictionay[key] = newTeams[key]
    print(myDictionary)
    """
    print(newTeams)
    myDictionary.update(newTeams)
    print(myDictionary)