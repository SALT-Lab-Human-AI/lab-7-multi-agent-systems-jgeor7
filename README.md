[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/3WjIbrgM)
# 🤖 Multi-Agent Systems Lab: AutoGen vs. CrewAI

## Basics and Fundamentals (!!Read this first!!)
Before diving into the lab, please read through the [BASICS.md](BASICS.md) file to understand key concepts about multi-agent systems, architectures, and communication patterns. This foundational knowledge will help you grasp the implementations in this lab.

## 📚 Lab Overview

This lab introduces **multi-agent systems** - where multiple AI agents collaborate to solve complex problems. You'll work with two popular frameworks (**AutoGen** and **CrewAI**) to build, compare, and understand how intelligent agents can work together.

### What You'll Learn
- How to design agents with specific roles and responsibilities
- How agents communicate and collaborate
- Differences between conversational (AutoGen) vs. task-based (CrewAI) approaches
- When to use each framework for different problem types

---

## 🎯 What Are We Building?

### Part 1: AutoGen - Product Planning Workflow
**Scenario:** Build a product plan for an AI-powered interview platform

Four agents work together in sequence:
1. **ResearchAgent** - Analyzes market competitors
2. **AnalysisAgent** - Identifies key opportunities
3. **BlueprintAgent** - Creates product design
4. **ReviewerAgent** - Provides recommendations

**Communication Style:** Conversational (agents chat back and forth)

### Part 2: CrewAI - Travel Planning Workflow
**Scenario:** Plan a 5-day trip to Iceland

Four agents form a "crew":
1. **FlightAgent** - Researches flights
2. **HotelAgent** - Finds accommodations
3. **ItineraryAgent** - Creates daily plans
4. **BudgetAgent** - Calculates costs

**Communication Style:** Task-based (each agent completes assigned tasks)

---

## 🛠️ Technologies Used

### **AutoGen** (Microsoft)
- Framework for building multi-agent systems with LLMs
- Agents communicate conversationally
- Flexible workflow - agents can decide what to do next
- Great for iterative, chat-like problem solving

```python
from autogen import AssistantAgent, UserProxyAgent

assistant = AssistantAgent(name="assistant", llm_config={"config_list": [...]})
user_proxy = UserProxyAgent(name="user_proxy", human_input_mode="NEVER")
user_proxy.initiate_chat(assistant, message="Your task here")
```

### **CrewAI** (Crew Framework)
- High-level framework for orchestrating agent "crews"
- Task-based execution - clear inputs and outputs
- Built-in tools and structured workflows
- Great for sequential, goal-oriented tasks

```python
from crewai import Agent, Task, Crew

agent = Agent(role="...", goal="...", backstory="...")
task = Task(description="...", agent=agent)
crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```

### **OpenAI API**
- Powers the language models both frameworks use
- GPT-4 or GPT-4-Turbo for intelligent reasoning

---

## 📖 Lab Manual

### Prerequisites
- Python 3.8+
- OpenAI API key (get from https://platform.openai.com/api-keys)
- `pip` package manager

### Quick Setup

**1. Configure API Key:**
```bash
# Copy template
cp .env.example .env

# Add your OpenAI API key
# Edit .env and add:
OPENAI_API_KEY=sk-your-api-key-here
```

**2. Install Dependencies:**
```bash
pip install -r requirements.txt
```

**3. Verify Configuration:**
```bash
python shared_config.py
```

### Running the Demos

**AutoGen Demo:**
```bash
python autogen/autogen_simple_demo.py
```

**CrewAI Demo:**
```bash
python crewai/crewai_demo.py
```

---

# Multi-Agent Systems Lab - Complete Guide

Welcome to the Multi-Agent Systems Lab! This project demonstrates the use of multi-agent frameworks for solving complex tasks, including travel planning and interview workflows. The lab is divided into two main frameworks:

1. **AutoGen**: A framework for building conversational agents.
2. **CrewAI**: A framework for orchestrating specialized agents to solve real-world problems.

---

## Project Structure

```
multi-agent/
├── README.md                          ← You are here (complete lab guide)
├── requirements.txt                   ← Install ALL dependencies from here
├── .env.example                       ← Copy to .env (don't commit!)
├── .env                               ← Your configuration (add API key here)
├── shared_config.py                   ← Unified config for both frameworks
│
├── autogen/
│   ├── config.py                      ← AutoGen configuration (uses shared_config)
│   ├── autogen_simple_demo.py         ← RUN THIS: Simple demo
│   └── autogen_interview_platform.py  ← Full implementation
│
└── crewai/
    └── crewai_demo.py                 ← RUN THIS: Travel planning demo
```

---

## Setup Instructions

### 1. Install Dependencies

Ensure you have Python 3.10+ installed. Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy the example `.env` file and add your OpenAI API key:

```bash
cp .env.example .env
```

Edit the `.env` file and add your OpenAI API key:

```
OPENAI_API_KEY=sk-...
```

---

## Running the Demos

### 1. AutoGen Framework

#### Simple Demo
Run the simple AutoGen demo to see a basic implementation:

```bash
python autogen/autogen_simple_demo.py
```

#### Full Implementation
Run the full AutoGen interview platform workflow:

```bash
python autogen/autogen_interview_platform.py
```

### 2. CrewAI Framework

Run the CrewAI travel planning demo to see agents collaborate on planning a trip:

```bash
python crewai/crewai_demo.py
```

---

## Key Files

### Configuration
- **`shared_config.py`**: Centralized configuration for both frameworks.
- **`.env`**: Environment variables (e.g., API keys).

### AutoGen
- **`autogen_simple_demo.py`**: A simple demo showcasing AutoGen capabilities.
- **`autogen_interview_platform.py`**: Full implementation of the interview platform.

### CrewAI
- **`crewai_demo.py`**: Travel planning demo using CrewAI.

---

## Notes

- Ensure your OpenAI API key has access to the required models (e.g., `gpt-4`).
- For any issues, check the OpenAI API status at [https://status.openai.com](https://status.openai.com).
- Do not commit your `.env` file to version control.

---

Happy experimenting with multi-agent systems!

