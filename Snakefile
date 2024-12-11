rule all:
    input:
        "results/age_distribution.png",
        "results/gender_distribution.png",
        "results/country_distribution.png",
        "results/state_distribution.png",
        "results/self_employment.png",
        "results/company_size.png",
        "results/remote_work_status.png",
        "results/tech_company_status.png",
        "results/mental_health_benefits.png",
        "results/care_options_awareness.png",
        "results/wellness_program.png",
        "results/negative_consequences.png",
        "results/coworker_discussion.png",
        "results/supervisor_discussion.png",
        "results/interview_discussion.png",
        "results/medical_leave.png",
        "results/anonymity_protection.png",
        "results/seek_help_resources.png",
        "results/observed_consequences.png"

rule plot_age_distribution:
    input: "data/survey.csv"
    output: "results/age_distribution.png"
    script:
        """
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns
        from scripts.data_analysis import plot_age_distribution

        df = pd.read_csv("data/survey.csv")
        plt.figure()
        plot_age_distribution(df)
        plt.savefig("results/age_distribution.png")
        plt.close()
        """

rule plot_gender_distribution:
    input: "data/survey.csv"
    output: "results/gender_distribution.png"
    script:
        """
        import pandas as pd
        import matplotlib.pyplot as plt
        from scripts.data_analysis import plot_gender_distribution

        df = pd.read_csv("data/survey.csv")
        plt.figure()
        plot_gender_distribution(df)
        plt.savefig("results/gender_distribution.png")
        plt.close()
        """

rule plot_country_distribution:
    input: "data/survey.csv"
    output: "results/country_distribution.png"
    script:
        """
        import pandas as pd
        import matplotlib.pyplot as plt
        from scripts.data_analysis import plot_country_distribution

        df = pd.read_csv("data/survey.csv")
        plt.figure()
        plot_country_distribution(df, top_n=10)
        plt.savefig("results/country_distribution.png")
        plt.close()
        """

rule plot_state_distribution:
    input: "data/survey.csv"
    output: "results/state_distribution.png"
    script:
        """
        import pandas as pd
        import matplotlib.pyplot as plt
        from scripts.data_analysis import plot_state_distribution

        df = pd.read_csv("data/survey.csv")
        plt.figure()
        plot_state_distribution(df)
        plt.savefig("results/state_distribution.png")
        plt.close()
        """

# Repeat similar rules for other plots

rule plot_self_employment:
    input: "data/survey.csv"
    output: "results/self_employment.png"
    script:
        """
        import pandas as pd
        import matplotlib.pyplot as plt
        from scripts.data_analysis import plot_self_employment

        df = pd.read_csv("data/survey.csv")
        plt.figure()
        plot_self_employment(df)
        plt.savefig("results/self_employment.png")
        plt.close()
        """

rule plot_company_size:
    input: "data/survey.csv"
    output: "results/company_size.png"
    script:
        """
        import pandas as pd
        import matplotlib.pyplot as plt
        from scripts.data_analysis import plot_company_size

        df = pd.read_csv("data/survey.csv")
        plt.figure()
        plot_company_size(df)
        plt.savefig("results/company_size.png")
        plt.close()
        """

# Continue with rules for remote work, tech company status, mental health benefits,
# care options awareness, wellness program, negative consequences, coworker discussion,
# supervisor discussion, interview discussion, medical leave, anonymity protection,
# seek help resources, and observed consequences.

