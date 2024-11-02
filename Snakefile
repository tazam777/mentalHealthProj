rule all:
    input:
        "results/cleaned_data.csv",
        "results/final_plot.png"

# Rule to process and clean data
rule process_data:
    input:
        agrofood="data/Agrofood_co2_emission.csv",
        gdp="data/gdp.csv"
    output:
        "results/cleaned_data.csv"
    script:
        "scripts/process_data.py"

# Rule to create the 4-panel plot from cleaned data
rule create_plot:
    input:
        "results/cleaned_data.csv"
    output:
        "results/final_plot.png"
    script:
        "scripts/create_plot.py"
