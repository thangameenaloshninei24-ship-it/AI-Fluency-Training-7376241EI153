# Agentic AI – Day 2 Lab

## Topic

ReAct, Chain-of-Thought Prompting, and Self-Consistency

## Objective

This lab explores how an LLM can:

- Reason through multi-step problems.
- Use external tools through the ReAct pattern.
- Compare direct prompting with Chain-of-Thought prompting.
- Generate multiple reasoning attempts using self-consistency.

## Project Structure

The Day 2 files are placed inside the existing Day 1 folder:

```text
day1_lab/
├── .venv/
├── .env
├── config.py
├── tools.py
├── agent.py
├── react_trace.py
├── cot_compare.py
└── self_consistency.py
```

The Day 2 programs reuse `config.py`, `tools.py`, and `agent.py` from Day 1.

## 1. ReAct

ReAct combines reasoning with tool usage:

```text
Thought → Action → Observation → Thought → ...
```

The agent uses:

```text
get_course_fee(course_code)
calculator(expression)
```

to solve a course-fee comparison problem.

Run:

```powershell
python react_trace.py
```

The expected result is that CS101 + AI202 with a 10% scholarship costs Rs. 27,000, which is Rs. 6,750 cheaper than all three courses with a 25% scholarship.

## 2. Chain-of-Thought Comparison

`cot_compare.py` compares:

```text
Without CoT → Final answer only
With CoT    → Step-by-step reasoning
```

It tests three problems involving arithmetic, counting, and logical ordering.

Run:

```powershell
python cot_compare.py
```

The purpose is to observe whether step-by-step prompting improves the model's answers and how it affects response length.

## 3. Self-Consistency

`self_consistency.py` runs the same Chain-of-Thought prompt multiple times and selects the most frequent final answer.

Configuration:

```python
RUNS = 5
TEMPERATURE = 0.8
```

Run:

```powershell
python self_consistency.py
```

A non-zero temperature allows different reasoning attempts, making majority voting meaningful.

## Key Learning

```text
CoT      → improves structured reasoning
ReAct    → combines reasoning with tools
Tools    → provide information the model does not have
Self-Consistency → compares multiple reasoning attempts
```

The main takeaway is that **reasoning and tool usage solve different problems**. Chain-of-Thought can help process given information, while ReAct allows the agent to obtain information and perform actions through tools.
