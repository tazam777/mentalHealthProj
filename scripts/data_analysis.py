import matplotlib.pyplot as plt
import seaborn as sns

def plot_age_distribution(df):
    """
    Plot the distribution of ages in the dataset.
    
    Args:
        df (pd.DataFrame): The DataFrame containing the 'Age' column.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'], bins=20, kde=True, color='blue')
    plt.title('Age Distribution of Respondents')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_gender_distribution(df):
    """
    Plot the distribution of gender in the dataset.
    
    Args:
        df (pd.DataFrame): The DataFrame containing the 'Gender' column.
    """
    plt.figure(figsize=(8, 6))
    df['Gender'].value_counts().plot(kind='bar', color='skyblue')
    plt.title('Gender Distribution')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()
