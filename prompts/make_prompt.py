#!/usr/bin/env python3

import os
import argparse
from openai import OpenAI

DEFAULT_MODEL = "gpt-4"

job_description ="""
OpenAsset - New York, NY
$150,000 - $195,000 a year

We are looking for a NYC or London based Staff Software Engineer - Frontend to join our talented, dynamic, and rapidly growing global team.

Company Description

OpenAsset is the only Digital Asset Management solution built for the Architecture, Construction and Engineering industries. We have over 800 clients and 20 years of experience delivering value. Our vision is to inspire people through visualization of the built world.

We are a diverse group of hard-working and entrepreneurial people dedicated to solving complex challenges, working hard on meaningful projects, and celebrating our successes. We are looking for extraordinary people to join our industry-leading and incredibly talented team! Our inspirational and fun working environment, innovation-driven, fast-growing company, and ambitious projects are just a few reasons why you will love working here.

As a company we are passionate about ensuring that diversity and inclusion are championed, and that everybody has a seat at the table. We promote a culture where everyone feels valued, and we have adopted policies to ensure we hire from a diverse pool of candidates.

OpenAsset employs 80 people and is growing rapidly. OpenAsset has partnered with Marlin Equity Partners, an $8bn private equity fund, to help the business scale its sales, technical and management capacity to meet accelerating demand for its B2B SaaS product.

Description

Embark on a rewarding journey as a Staff Software Engineer - Frontend at OpenAsset, leading the charge of our dynamic frontend team. In this hands-on technical role, you'll be at the forefront of crafting exceptional user experiences using React, TypeScript, and JavaScript. As a pivotal force in our team, you will not only contribute directly to code but also champion best practices, guide the team through technical challenges, and advocate for excellence in all aspects of software development.

Your expertise will shape the technical direction of our applications, ensuring they remain scalable, performant, and maintainable. If you're passionate about delving into the intricacies of frontend technologies, mentoring fellow engineers, and making a tangible impact on product delivery, we invite you to be a driving force in our collaborative and forward-thinking environment. Join us, where your hands-on technical leadership will be instrumental in the success of our projects and the growth of our talented team.

Responsibilities

As a Staff Software Engineer - Frontend, your day-to-day activities will revolve around technical leadership, effective communication, and a hands-on approach to solving complex challenges, contributing to the overall success of the frontend team and the company.

Project Ownership

Lead the design, planning, estimation, testing, and coordination for ongoing and upcoming team projects spanning multiple releases.
Take ownership of the entire development lifecycle, ensuring the delivery of complex systems on time and within budget.
Cross-Team Collaboration

Collaborate with Product and Engineering teams to address cross-cutting technical issues, contributing to the overall success of company-wide initiatives.
Work on issues requiring in-depth evaluation, providing creative and effective solutions to complex problems.
Technical Leadership

Provide technical advice and weigh in on decisions that have an impact on other teams or the company at large.
Research and propose new technologies to enhance the capabilities of the frontend applications.
Communication and Mentorship

Communicate effectively within and outside the Engineering organization, fostering a collaborative environment.
Contribute to the growth of team members through code reviews, documentation, technical guidance, and mentorship.
Strategic Problem Solving

Actively identify and propose strategies to resolve technical problems affecting the team, demonstrating a strategic mindset.
Determine methods and procedures used by the team, focusing on continuous improvement and efficiency.
Security, Reliability, and Compliance

Actively work to refine the team’s approach to security, reliability, privacy, and compliance.
Complete tasks and projects in these areas with minimal guidance, ensuring the highest standards are met.
Documentation and Knowledge Sharing

Take responsibility for team and system-wide documentation, ensuring that knowledge is well-documented and shared within the team and beyond.
Skills and Experience

7+ years of frontend engineering experience
3+ years of technical leadership experience and/or managing teams
High proficiency in Javascript, Typescript, React, and HTML/CSS
Strong systems and UI architecture skills and experience working with multiple systems and their UIs at scale
Deep understanding of continuous refactoring for reusability and testability
Experience leading and mentoring engineers without formal direct reporting relationships
Proactively collaborating with different engineering teams and advocating for team’s needs
Working in an Agile/Scrum methodology
Bachelors or Masters in Computer Science, Engineering or other related technical field
Technologies we use

React
GraphQL
Typescript
SASS
Jest
Github (and Github actions)
CircleCI
Webpack
Flux
Babel
PostCSS
Python
Terraform
Docker
AWS
Benefits

Competitive salary
Medical / Dental / Vision coverage
20 days paid time off per year + federal holidays (UK style!)
5 paid sick days
Work from home flexibility
Commuter benefits
401k
Paid parental leave
Career growth and development opportunities
This position is not eligible for visa sponsorship.

Axomic is an Equal Opportunity Employer. We base our employment decisions entirely on business needs, job requirements, and qualifications—we do not discriminate based on race, gender, religion, health, parental status, personal beliefs, veteran status, age, or any other status. We have zero tolerance for any kind of discrimination, and we are looking for candidates who share those values. Applications from women and members of underrepresented minority groups are welcomed.

Job Type: Full-time

Pay: $150,000.00 - $195,000.00 per year

Benefits:

401(k)
Dental insurance
Flexible schedule
Health insurance
Paid time off
Parental leave
Referral program
Vision insurance
Schedule:

Monday to Friday
Work Location: Hybrid remote in New York, NY 1001.
"""

def make_payload(job_description):
  return  {
    "model" : "gpt-4",
    "messages": [
      {
        "role": "system",
        "content": (
            "Perform a focused internet search on OpenAsset to obtain key information relevant to provided job offer listing."
            "Concentrate on extracting concise, pertinent details that will directly assist in tailoring a resume for the specific job offer."
        )
      },
      {
        "role": "user",
        "content": f"I have a job offer listing from OpenAsset. Here it is:\n {job_description}. I need you to quickly find and summarize the most important information about OpenAsset that I should include in my resume for this job."
      }
    ]
  }


def get_api_key():
    return os.getenv('OPENAI_API_KEY')


def main():
    openai_client = OpenAI(api_key=get_api_key())

    payload = make_payload(job_description)

    response = openai_client.chat.completions.create(**payload)
    py_response = response.model_dump()

    content = py_response['choices'][0]['message']['content']

    print(content)


if __name__ == '__main__':
    main()
