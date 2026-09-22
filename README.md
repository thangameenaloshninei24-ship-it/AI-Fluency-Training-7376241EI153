Day 1 Task: Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent
About This Task
This project is part of Unit 1: Foundations of AI Agents.

The purpose of this task is to compare three different approaches to solving the same private-data problem:

A plain chatbot
A rule-based workflow
An AI agent
The task demonstrates the difference between a chatbot that mainly uses an LLM to provide responses, a rule-based workflow that follows predefined steps and conditions, and an AI agent that combines an LLM, tools, and a loop.

Task Objective
For this project, I selected a small private-data scenario and implemented it using all three approaches.

The same user request is handled by each approach so that their differences can be compared.

The comparison focuses on:

Flexibility
Decision-making
Tool usage
Private-data access
Multi-step task handling
Automation
Reliability
Private-Data Scenario
The scenario selected for this project is a private expense-tracking problem.

The private expense data is stored in:

expenses.txt

The user can ask a question such as:

How much did I spend on food?

Each of the three approaches handles this request differently.

Approaches
1. Plain Chatbot
The plain chatbot mainly provides a response using an LLM.

It does not independently select or use external tools to complete the task.

2. Rule-Based Workflow
The rule-based workflow follows predefined programming steps and conditions.

There is no LLM involved.

The workflow processes the expense data according to fixed rules and produces the result.

3. AI Agent
The AI agent follows the foundation:

Agent = LLM + Tools + Loop

The agent can interpret the user's request, select and use appropriate tools, observe the results, and continue taking actions until the task is completed.

This allows the agent to handle a more dynamic, multi-step task compared with a fixed rule-based workflow.

Repository Contents
chatbot.py - implementation of the plain chatbot
workflow.py - implementation of the rule-based workflow
agent.py - implementation of the AI agent
expenses.txt - private expense data used in the scenario
analysis.md - detailed explanation, comparison table, suitability analysis, and conclusion
requirements.txt - project dependencies
Output/ - screenshots showing the three systems running
Expected Result
The project demonstrates how the same private-data problem can be approached using:

LLM response → Plain Chatbot

Predefined rules → Rule-Based Workflow

LLM + Tools + Loop → AI Agent

The project also explains the limitations and appropriate use cases of each approach.

Conclusion
A plain chatbot, a rule-based workflow, and an AI agent solve problems in different ways.

A chatbot is mainly focused on generating responses.

A rule-based workflow follows predefined instructions and conditions.

An AI agent combines an LLM with tools and a loop so that it can reason about a task, use tools, observe results, and continue working until the task is completed.
