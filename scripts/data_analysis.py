import matplotlib.pyplot as plt
import seaborn as sns

def plot_age_distribution(df):
    """Plots the distribution of age."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'], bins=20, kde=True, color='blue')
    plt.title('Age Distribution of Respondents')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_gender_distribution(df):
    """Plots the distribution of gender."""
    plt.figure(figsize=(8, 6))
    df['Gender'].value_counts().plot(kind='bar', color='skyblue')
    plt.title('Gender Distribution')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_country_distribution(df, top_n=10):
    """Plots the distribution of respondents by country."""
    plt.figure(figsize=(12, 6))
    df['Country'].value_counts().head(top_n).plot(kind='bar', color='lightgreen')
    plt.title(f'Top {top_n} Countries of Respondents')
    plt.xlabel('Country')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_state_distribution(df):
    """Plots the distribution of respondents by state for the USA."""
    plt.figure(figsize=(12, 6))
    df[df['Country'] == 'United States']['state'].value_counts().head(10).plot(kind='bar', color='lightcoral')
    plt.title('Top 10 States in the USA')
    plt.xlabel('State')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_self_employment(df):
    """Plots the distribution of self-employment status."""
    plt.figure(figsize=(8, 6))
    df['self_employed'].value_counts().plot(kind='bar', color='lightblue')
    plt.title('Self-Employment Status')
    plt.xlabel('Self-Employed')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_company_size(df):
    """Plots the distribution of company size."""
    plt.figure(figsize=(8, 6))
    df['no_employees'].value_counts().plot(kind='bar', color='lightblue')
    plt.title('Company Size')
    plt.xlabel('Number of Employees')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.xticks(rotation=45)
    plt.show()

def plot_remote_work_status(df):
    """Plots the distribution of remote work status."""
    plt.figure(figsize=(8, 6))
    df['remote_work'].value_counts().plot(kind='bar', color='lightgreen')
    plt.title('Remote Work Status')
    plt.xlabel('Remote Work')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_tech_company_status(df):
    """Plots the distribution of tech company employment status."""
    plt.figure(figsize=(8, 6))
    df['tech_company'].value_counts().plot(kind='bar', color='orange')
    plt.title('Tech Company Employment')
    plt.xlabel('Tech Company')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_mental_health_benefits(df):
    """Plots the distribution of mental health benefits provided by employers."""
    plt.figure(figsize=(8, 6))
    df['benefits'].value_counts().plot(kind='bar', color='purple')
    plt.title('Does Employer Provide Mental Health Benefits?')
    plt.xlabel('Mental Health Benefits')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_care_options_awareness(df):
    """Plots the distribution of awareness of mental health care options."""
    plt.figure(figsize=(8, 6))
    df['care_options'].value_counts().plot(kind='bar', color='lightblue')
    plt.title('Awareness of Employer Mental Health Care Options')
    plt.xlabel('Care Options Awareness')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_wellness_program(df):
    """Plots the distribution of wellness programs that include mental health."""
    plt.figure(figsize=(8, 6))
    df['wellness_program'].value_counts().plot(kind='bar', color='lightgreen')
    plt.title('Mental Health as Part of Wellness Program?')
    plt.xlabel('Wellness Program')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_negative_consequences(df):
    """Plots the distribution of negative consequences for discussing mental health at work."""
    plt.figure(figsize=(8, 6))
    df['mental_health_consequence'].value_counts().plot(kind='bar', color='red')
    plt.title('Negative Consequences of Discussing Mental Health at Work')
    plt.xlabel('Mental Health Consequence')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_coworker_discussion(df):
    """Plots the distribution of comfort discussing mental health with coworkers."""
    plt.figure(figsize=(8, 6))
    df['coworkers'].value_counts().plot(kind='bar', color='blue')
    plt.title('Discussing Mental Health with Coworkers')
    plt.xlabel('Coworkers')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_supervisor_discussion(df):
    """Plots the distribution of comfort discussing mental health with supervisors."""
    plt.figure(figsize=(8, 6))
    df['supervisor'].value_counts().plot(kind='bar', color='orange')
    plt.title('Discussing Mental Health with Supervisors')
    plt.xlabel('Supervisor')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_interview_discussion(df):
    """Plots the distribution of comfort discussing mental health in job interviews."""
    plt.figure(figsize=(8, 6))
    df['mental_health_interview'].value_counts().plot(kind='bar', color='purple')
    plt.title('Discussing Mental Health in Job Interviews')
    plt.xlabel('Mental Health in Interviews')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_medical_leave(df):
    """Plots the ease of taking medical leave for mental health reasons."""
    plt.figure(figsize=(8, 6))
    df['leave'].value_counts().plot(kind='bar', color='skyblue')
    plt.title('Ease of Taking Medical Leave for Mental Health')
    plt.xlabel('Medical Leave')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_anonymity_protection(df):
    """Plots the distribution of anonymity protection in seeking mental health help."""
    plt.figure(figsize=(8, 6))
    df['anonymity'].value_counts().plot(kind='bar', color='lightgreen')
    plt.title('Anonymity Protection in Seeking Mental Health Help')
    plt.xlabel('Anonymity Protection')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_seek_help_resources(df):
    """Plots the distribution of employer resources for seeking mental health help."""
    plt.figure(figsize=(8, 6))
    df['seek_help'].value_counts().plot(kind='bar', color='orange')
    plt.title('Employer Resources for Seeking Mental Health Help')
    plt.xlabel('Seek Help')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_observed_consequences(df):
    """Plots the distribution of observed negative consequences for discussing mental health at work."""
    plt.figure(figsize=(8, 6))
    df['obs_consequence'].value_counts().plot(kind='bar', color='red')
    plt.title('Observed Negative Consequences for Mental Health Discussion')
    plt.xlabel('Observed Consequences')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()
