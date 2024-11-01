import pandas as pd
import pycountry

def load_data(file_path):
    """
    Load data from a CSV file and convert 'Timestamp' column to datetime format.
    
    Args:
        file_path (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Loaded and preprocessed DataFrame.
    """
    df = pd.read_csv(file_path)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    # Additional data cleaning steps can be added here as needed.
    return df

def clean_gender(gender):
    """
    Clean and standardize the 'Gender' column to ensure consistency.
    
    Args:
        gender (str): Raw gender value.
        
    Returns:
        str: Standardized gender value.
    """
    gender = gender.strip().lower()  # Normalize string by stripping spaces and converting to lowercase
    if gender in ['male', 'm', 'man', 'cis male', 'male (cis)', 'male ']:
        return 'Male'
    elif gender in ['female', 'f', 'woman', 'cis female', 'female ', 'femake', 'femail']:
        return 'Female'
    elif gender in ['trans male', 'trans man', 'ftm', 'trans-male']:
        return 'Trans Male'
    elif gender in ['trans female', 'trans woman', 'mtf', 'trans-female']:
        return 'Trans Female'
    elif gender in ['non-binary', 'genderqueer', 'androgyne', 'agender', 'enby', 'fluid', 'neuter', 
                    'queer', 'queer/she/they', 'male leaning androgynous', 'something kinda male?', 
                    'genderqueer']:
        return 'Non-binary/Other'
    else:
        return 'Non-binary/Other'  # Default category for unclear/ambiguous gender identities

def standardize_country(country_name):
    """
    Standardize country names using the pycountry library with common variations.
    
    Args:
        country_name (str): Raw country name.
        
    Returns:
        str: Standardized country name or original if not found.
    """
    # Common manual corrections
    manual_mappings = {
        'Brasil': 'Brazil',
        'Estados Unidos': 'United States',
        'UK': 'United Kingdom',
        'U.S.A.': 'United States',
        'USA': 'United States'
    }
    
    # Check for manual mappings first
    if country_name in manual_mappings:
        return manual_mappings[country_name]

    # Normalize case before lookup
    try:
        standardized_name = pycountry.countries.lookup(country_name.strip().title()).name
        return standardized_name
    except LookupError:
        # Return the original input without altering the case
        return country_name.strip()
