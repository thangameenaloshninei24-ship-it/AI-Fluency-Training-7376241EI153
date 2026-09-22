Day 1 Lab — Chatbot vs Rule-Based Workflow vs AI Agent
Agentic AI: Foundations and Open-Source Practice
This project is part of Day 1: Foundations of AI Agents.

The purpose of this lab is to set up a Python environment in VS Code, connect Python to an open Large Language Model (LLM), and compare three different approaches to solving the same problem:

Plain LLM Chatbot
Rule-Based Workflow
Tool-Using AI Agent
The lab demonstrates the difference between an LLM, a fixed workflow, and an AI agent that can use tools in a loop.

Problem Statement
A college has private course-fee information:

Course	Fee
CS101	Rs. 12,000
AI202	Rs. 18,000
DS303	Rs. 15,000
The three systems are tested using the same questions.

Test Questions
What is the fee for AI202?
What is the total fee for CS101 and AI202 after a 10% scholarship?
Is DS303 more expensive than CS101, and by how much?
Write a two-line welcome message for new AI students.
Expected factual answers
AI202 fee: Rs. 18,000
CS101 + AI202 after 10% scholarship: Rs. 27,000
DS303 is more expensive than CS101 by Rs. 3,000
Question 4 does not require private course-fee data.
Systems Implemented
1. Plain LLM Chatbot
The chatbot sends the user's question directly to the LLM.

It has:

No access to the college's private fee data
No tools
No external calculation mechanism
Because the private fee information is not provided to the model, it may produce incorrect but confident answers to questions requiring that data.

2. Rule-Based Workflow
The workflow is implemented using fixed Python rules.

It has:

No LLM
No tool-calling loop
Predefined conditions written by the programmer
Direct access to the course-fee dictionary
It can reliably answer questions that match the rules, but it may fail when the question is phrased differently or when a new type of question is asked.

3. AI Agent
The AI agent combines:

LLM + Tools + Loop

The agent can decide when to use available tools.

The project provides two tools:

get_course_fee — looks up the fee for a course
calculator — performs arithmetic safely
The agent follows a reason → act → observe process:

The LLM determines what action is needed.
The Python program executes the selected tool.
The result is returned to the LLM.
The agent continues until it can produce a final answer or reaches the maximum step limit.
The printed tool-call trace is used to observe this process.

Project Structure
DAY1_TASK/
│
├── .env
├── .gitignore
├── requirements.txt
│
├── config.py
├── check_setup.py
├── chatbot.py
├── workflow.py
├── tools.py
├── agent.py
├── challenge.py
│
├── README.md
├── analysis.md
│
├── Output/
│   ├── chatbot_output.png
│   ├── workflow_output.png
│   ├── agent_output.png
│   └── challenge_output.png
│
└── .venv/
.env must not be uploaded to GitHub because it may contain an API key or token.

Technologies Used
Python 3.11+
Visual Studio Code
Python extension for VS Code
OpenAI Python package
python-dotenv
Ollama, Groq, or Hugging Face
OpenAI-compatible API
The lab supports three LLM provider options:

Ollama with a local model
Groq with a free API key
Hugging Face with a free token
Only the .env configuration changes between providers.

Installation
Create and activate the virtual environment:

Windows PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1
If PowerShell blocks activation:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
Install the required packages:

pip install -r requirements.txt
Running the Lab
First check the environment and LLM connection:

python check_setup.py
The setup check should finish with:

Model replied : SETUP OK
Setup check finished.
Then run the three systems:

python chatbot.py
python workflow.py
python agent.py
Run the additional challenge:

python challenge.py
Challenge Question
The additional challenge asks:

I can pay Rs. 30,000. Which two courses can I take together within this budget?

The workflow has no predefined rule for this type of question.

The agent can use the course-fee lookup and calculator tools to investigate possible combinations.

The expected pair within the budget is:

CS101 + DS303 = Rs. 27,000

Small local models may not always solve this correctly, so the actual result should be recorded in the observations.

Learning Outcomes
This lab demonstrates that:

A plain chatbot can generate useful language but does not automatically know private data.
A rule-based workflow can be predictable for cases covered by its rules.
Fixed rules can become rigid when users change their wording or ask new types of questions.
An AI agent can use tools and perform multiple steps to solve a problem.
Agent behaviour can be less predictable because the LLM decides which tools to use.
Tool traces help show the agent's reason → act → observe process.
Observation and Analysis
The results of the actual runs are recorded separately in:

analysis.md
The analysis compares the chatbot, workflow, and agent using:

Correctness
Flexibility
Decision-making
Tool usage
Private-data access
Multi-step task handling
Automation
Reliability
Response time
Number of LLM calls
Strengths and weaknesses
Suitable real-world use cases
Screenshots of the outputs are stored in the:

Output/
folder.

Conclusion
The lab compares three approaches to the same private-data problem.

The chatbot relies only on the LLM, the rule-based workflow relies on predefined Python logic, and the AI agent combines an LLM with tools and an iterative loop.

The final observations and analysis are based on the actual outputs produced during the lab.
