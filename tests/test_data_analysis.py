import pytest
import pandas as pd
from scripts.data_analysis import (
    plot_age_distribution,
    plot_gender_distribution,
    plot_country_distribution,
    plot_state_distribution,
    plot_self_employment,
    plot_company_size,
    plot_remote_work_status,
    plot_tech_company_status,
    plot_mental_health_benefits,
    plot_care_options_awareness,
    plot_wellness_program,
    plot_negative_consequences,
    plot_coworker_discussion,
    plot_supervisor_discussion,
    plot_interview_discussion,
    plot_medical_leave,
    plot_anonymity_protection,
    plot_seek_help_resources,
    plot_observed_consequences
)

# Set matplotlib to use 'Agg' backend for tests (no GUI required)
import matplotlib
matplotlib.use('Agg')

@pytest.fixture
def sample_dataframe():
    data = {
        'Age': [25, 32, 40, 28, 22],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Non-binary/Other'],
        'Country': ['United States', 'Canada', 'United Kingdom', 'France', 'Germany'],
        'state': ['CA', 'ON', 'NY', 'QC', 'TX'],
        'self_employed': ['No', 'Yes', 'No', 'No', 'Yes'],
        'no_employees': ['1-5', '6-25', '26-100', '100-500', '500-1000'],
        'remote_work': ['Yes', 'No', 'Yes', 'No', 'Yes'],
        'tech_company': ['Yes', 'No', 'Yes', 'Yes', 'No'],
        'benefits': ['Yes', 'No', 'Yes', 'No', 'Don\'t know'],
        'care_options': ['Yes', 'No', 'Not sure', 'Yes', 'No'],
        'wellness_program': ['Yes', 'No', 'Don\'t know', 'Yes', 'No'],
        'leave': ['Somewhat easy', 'Very difficult', 'Don\'t know', 'Very easy', 'Somewhat difficult'],
        'mental_health_consequence': ['No', 'Yes', 'Maybe', 'No', 'Yes'],
        'coworkers': ['Yes', 'No', 'Some of them', 'Yes', 'No'],
        'supervisor': ['Yes', 'No', 'Some of them', 'Yes', 'No'],
        'mental_health_interview': ['No', 'Yes', 'Maybe', 'No', 'Yes'],
        'phys_health_interview': ['Yes', 'No', 'Maybe', 'Yes', 'No'],
        'anonymity': ['Yes', 'No', 'Don\'t know', 'Yes', 'No'],
        'seek_help': ['Yes', 'No', 'Don\'t know', 'Yes', 'No'],
        'obs_consequence': ['No', 'Yes', 'No', 'No', 'Yes']
    }
    return pd.DataFrame(data)

def test_plot_age_distribution(sample_dataframe):
    """Test age distribution plot"""
    plot_age_distribution(sample_dataframe)

def test_plot_gender_distribution(sample_dataframe):
    """Test gender distribution plot"""
    plot_gender_distribution(sample_dataframe)

def test_plot_country_distribution(sample_dataframe):
    """Test country distribution plot"""
    plot_country_distribution(sample_dataframe, top_n=5)

def test_plot_state_distribution(sample_dataframe):
    """Test state distribution plot"""
    plot_state_distribution(sample_dataframe)

def test_plot_self_employment(sample_dataframe):
    """Test self-employment plot"""
    plot_self_employment(sample_dataframe)

def test_plot_company_size(sample_dataframe):
    """Test company size plot"""
    plot_company_size(sample_dataframe)

def test_plot_remote_work_status(sample_dataframe):
    """Test remote work status plot"""
    plot_remote_work_status(sample_dataframe)

def test_plot_tech_company_status(sample_dataframe):
    """Test tech company status plot"""
    plot_tech_company_status(sample_dataframe)

def test_plot_mental_health_benefits(sample_dataframe):
    """Test mental health benefits plot"""
    plot_mental_health_benefits(sample_dataframe)

def test_plot_care_options_awareness(sample_dataframe):
    """Test care options awareness plot"""
    plot_care_options_awareness(sample_dataframe)

def test_plot_wellness_program(sample_dataframe):
    """Test wellness program plot"""
    plot_wellness_program(sample_dataframe)

def test_plot_negative_consequences(sample_dataframe):
    """Test negative consequences plot"""
    plot_negative_consequences(sample_dataframe)

def test_plot_coworker_discussion(sample_dataframe):
    """Test coworker discussion plot"""
    plot_coworker_discussion(sample_dataframe)

def test_plot_supervisor_discussion(sample_dataframe):
    """Test supervisor discussion plot"""
    plot_supervisor_discussion(sample_dataframe)

def test_plot_interview_discussion(sample_dataframe):
    """Test interview discussion plot"""
    plot_interview_discussion(sample_dataframe)

def test_plot_medical_leave(sample_dataframe):
    """Test medical leave plot"""
    plot_medical_leave(sample_dataframe)

def test_plot_anonymity_protection(sample_dataframe):
    """Test anonymity protection plot"""
    plot_anonymity_protection(sample_dataframe)

def test_plot_seek_help_resources(sample_dataframe):
    """Test seek help resources plot"""
    plot_seek_help_resources(sample_dataframe)

def test_plot_observed_consequences(sample_dataframe):
    """Test observed consequences plot"""
    plot_observed_consequences(sample_dataframe)
