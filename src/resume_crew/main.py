#!/usr/bin/env python
import sys
import warnings
from resume_crew.crew import ResumeCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the resume optimization crew.
    """
    inputs = {
        "job_url": "https://www.linkedin.com/jobs/view/4132705547/?refId=8fd9bad3-622f-4a66-85ae-ecf72a8c99e2&trackingId=lJm44rZ7TCycAjJ%2FEbhu7w%3D%3D",
        "company_name": "Harnham",
    }
    ResumeCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
