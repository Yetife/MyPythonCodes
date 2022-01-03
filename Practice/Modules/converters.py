# modules is used to organise our code into multiple files

def lbs_to_kg(weight):
    weight = weight * 0.45
    return f'{weight}kg'

def kg_to_lbs(weight):
    weight = weight / 0.45
    return f'{weight}lbs'