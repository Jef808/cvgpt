#!/usr/bin/env python3

import sys
from pathlib import Path
from common import notify, get_api_key, do_prompt, get_job_description_and_company_name

def make_payload(cvjson, company_data, job_description_summary, company_name):

 # print(cvjson)
 # print(job_description)
 # print(company_data)
 # print(companyname)
  return  {
    "model" : "gpt-3.5-turbo",
    "messages": [

      {
        "role": "system",
        "content": f"Utilize the job description summary that will provided , the company name, and company data to make targeted improvements to the resume, which is a JSON represention of a CV. Focus on concise and direct enhancements that align the resume more closely with the specific requirements of the job description."
      },
      {
        "role": "user",
        "content": f"Here's the summary of the job description ({job_description_summary}), information about the company ({company_name}, {company_data}), and my current resume ({cvjson}). I need to modify my resume in a way that is concise and directly aligns with the job requirements."
      }

    ]
  }

def main(cvjsonpath, jobdescriptionsummarypath , companydatapath, companyname ):
  
    notify("starting script: " + __file__)
    cvjson = open(cvjsonpath, 'r').read()
    jobdescriptionsummary = open(jobdescriptionsummarypath , 'r').read()
    companydata = open(companydatapath , 'r').read()

    payload = make_payload(cvjson, companydata, jobdescriptionsummary, companyname)
    response = do_prompt(payload)
    print(response)


if __name__ == '__main__':
  cvjsonpath = Path(sys.argv[1])
  jobdescriptionsummarypath = Path(sys.argv[2])
  companydatapath = Path(sys.argv[3])
  companyname  = Path(sys.argv[4])
  main(cvjsonpath, jobdescriptionsummarypath , companydatapath, companyname )
