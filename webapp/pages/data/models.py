import pandas as pd
from webapp.pages.data.crud import AnimalShelter

# instantiate the class object to access the database
shelter = AnimalShelter()

# Retrieve and store collection documents into dataframe
df = pd.DataFrame.from_records(shelter.read({}))

# Copy the dataframe to avoid accidental database modifications
dff = df.copy()

# Modify age in weeks column to display rounded value with no decimal
dff.iloc[:, 15] = dff.iloc[:, 15].round(0)

# Columns to display in UI
display_columns = [
                {"name": "Age (weeks)", "id": 'age_upon_outcome_in_weeks', "deletable": False, "selectable": True},
                {"name": "Animal Type", "id": 'animal_type', "deletable": False, "selectable": True},
                {"name": "Breed", "id": 'breed', "deletable": False, "selectable": True},
                {"name": "Name", "id": 'name', "deletable": False, "selectable": True},
                {"name": "Sex", "id": 'sex_upon_outcome', "deletable": False, "selectable": True},
                ]

# rescue animal filter
animal_filter = ['Dog']

# animal sex filter
female = ['Intact Female']
male = ['Intact Male']

# filter for water rescue dog breeds
water_breeds = [
    'Labrador Retriever Mix',
    'Chesa Bay Retr Mix',
    'Newfoundland Mix',
    'Newfoundland/Labrador Retriever', 
    'Newfoundland/Australian Cattle Dog',
    'Newfoundland/Great Pyrenees'
    ]

# filter for mountain / wilderness resce dog breeds
mount_breeds = [
    'German Shepherd',
    'Alaskan Malamute',
    'Old English',
    'Sheepdog',
    'Siberian Husky',
    'Rottweiler'
    ]

# filter for disaster / individual rescue dog breeds
disast_breeds = [
    'Doberman Pinsch',
    'German Shepherd',
    'Golden Retriever',
    'Bloodhound', 
    'Rottweiler'
    ]

# age filters per rescue types
age_min_1 = 26
age_max_1 = 156
age_min_2 = 20
age_max_2 = 300

# Water rescue dogs
dff.loc[(dff.animal_type.isin(animal_filter)) &
        (dff.sex_upon_outcome.isin(female)) &
        (dff.breed.isin(water_breeds)) &
        (dff.age_upon_outcome_in_weeks.between(age_min_1, age_max_1)), 'rescue_type'] = 'Water'

# Mountain / Wilderness rescue dogs
dff.loc[(dff.animal_type.isin(animal_filter)) &
        (dff.sex_upon_outcome.isin(male)) &
        (dff.breed.isin(mount_breeds)) &
        (dff.age_upon_outcome_in_weeks.between(age_min_1, age_max_1)), 'rescue_type'] = 'Mountain/Wilderness'

# Disaster individual rescue dogs
dff.loc[(dff.animal_type.isin(animal_filter)) &
        (dff.sex_upon_outcome.isin(male)) &
        (dff.breed.isin(disast_breeds)) &
        (dff.age_upon_outcome_in_weeks.between(age_min_2, age_max_2)), 'rescue_type'] = 'Disaster/Individual'

# filtered Dataframe based on user selection in UI
df_filter = dff[['rescue_type', 'animal_type', 'sex_upon_outcome', 'breed', 'age_upon_outcome_in_weeks']]