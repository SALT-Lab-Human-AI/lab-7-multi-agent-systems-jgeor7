#!/usr/bin/env python3
"""
Multi-Agent Use Cases Demo
==========================

This script demonstrates how to use CrewAI and AutoGen for various professional tasks:
1. Plan a 3-day conference agenda
2. Design a marketing strategy for a product  
3. Create a research paper outline
4. Plan a software architecture

Each use case shows specialized agent configurations and workflows.
"""

import sys
from pathlib import Path

# Add autogen directory for config
sys.path.insert(0, str(Path(__file__).parent / "autogen"))

print("🚀 Multi-Agent Use Cases Demo")
print("=" * 60)

# ============================================================================
# USE CASE 1: 3-Day Conference Agenda Planning (CrewAI)
# ============================================================================
print("\n📅 USE CASE 1: Conference Planning")
print("-" * 40)

try:
    from crewai import Agent, Task, Crew

    # Conference Planning Agent
    conference_planner = Agent(
        role="Senior Conference Program Manager",
        goal="Design engaging and well-structured conference agendas that maximize learning and networking opportunities",
        backstory="""You are an experienced event planner with 12+ years organizing tech conferences, 
        academic symposiums, and industry summits. You understand audience engagement, speaker logistics, 
        timing optimization, and creating memorable experiences. You've successfully planned over 200 events.""",
        verbose=False
    )

    conference_task = Task(
        description="""Plan a 3-day AI & Machine Learning conference agenda for 300 attendees. Include:
        - Daily themes and focus areas
        - Keynote speakers and session topics  
        - Break timing and networking opportunities
        - Workshop sessions and hands-on labs
        - Panel discussions and Q&A sessions
        - Meals and social events""",
        agent=conference_planner,
        expected_output="Detailed 3-day conference schedule with times, speakers, and session descriptions"
    )

    conference_crew = Crew(
        agents=[conference_planner],
        tasks=[conference_task],
        verbose=False
    )

    print("Planning 3-day conference agenda...")
    conference_result = conference_crew.kickoff()
    print("✅ Conference agenda created!")
    print("Preview:", str(conference_result)[:200] + "...")

except Exception as e:
    print(f"❌ Conference planning failed: {e}")

# ============================================================================
# USE CASE 2: Marketing Strategy (CrewAI)
# ============================================================================
print("\n📈 USE CASE 2: Marketing Strategy Design")
print("-" * 40)

try:
    # Marketing Strategist Agent
    marketing_strategist = Agent(
        role="Senior Marketing Strategy Director", 
        goal="Develop comprehensive marketing strategies that drive customer acquisition and brand growth",
        backstory="""You are a seasoned marketing executive with expertise in digital marketing, 
        brand positioning, customer segmentation, and growth hacking. You've launched successful 
        campaigns for Fortune 500 companies and startups, with deep knowledge of modern marketing 
        channels and data-driven strategies.""",
        verbose=False
    )

    marketing_task = Task(
        description="""Design a comprehensive marketing strategy for a new AI-powered productivity app. Include:
        - Target audience analysis and personas
        - Brand positioning and unique value proposition  
        - Marketing channel mix (digital, content, social, etc.)
        - Campaign timeline and budget allocation
        - Key performance indicators and success metrics
        - Competitive differentiation strategy""",
        agent=marketing_strategist,
        expected_output="Complete marketing strategy document with actionable tactics and measurable goals"
    )

    marketing_crew = Crew(
        agents=[marketing_strategist],
        tasks=[marketing_task], 
        verbose=False
    )

    print("Developing marketing strategy...")
    marketing_result = marketing_crew.kickoff()
    print("✅ Marketing strategy created!")
    print("Preview:", str(marketing_result)[:200] + "...")

except Exception as e:
    print(f"❌ Marketing strategy failed: {e}")

# ============================================================================
# USE CASE 3: Research Paper Outline (AutoGen)
# ============================================================================
print("\n📝 USE CASE 3: Research Paper Outline")
print("-" * 40)

try:
    from autogen import ConversableAgent
    from config import Config
    
    config_list = Config.get_config_list()

    # Research Paper Agent
    research_agent = ConversableAgent(
        name="ResearchScholar",
        system_message="""You are a distinguished academic researcher with expertise in computer science 
        and artificial intelligence. You have published 50+ peer-reviewed papers and understand research 
        methodology, literature review processes, and academic writing standards. You excel at creating 
        well-structured research outlines that follow academic conventions.""",
        llm_config={"config_list": config_list, "temperature": 0.7},
        human_input_mode="NEVER"
    )

    user_proxy = ConversableAgent(
        name="ResearchDirector", 
        system_message="You initiate research tasks and coordinate academic projects.",
        llm_config={"config_list": config_list, "temperature": 0.7},
        human_input_mode="NEVER"
    )

    print("Creating research paper outline...")
    research_result = user_proxy.initiate_chat(
        research_agent,
        message="""Create a detailed outline for a research paper on "Ethical AI in Healthcare: 
        Balancing Innovation and Patient Privacy". Include abstract structure, introduction, 
        literature review sections, methodology, expected results, and conclusion frameworks.""",
        max_turns=2
    )
    print("✅ Research paper outline created!")

except Exception as e:
    print(f"❌ Research paper outline failed: {e}")

# ============================================================================  
# USE CASE 4: Software Architecture Planning (CrewAI)
# ============================================================================
print("\n🏗️ USE CASE 4: Software Architecture Planning")
print("-" * 40)

try:
    # Software Architect Agent
    software_architect = Agent(
        role="Principal Software Architect",
        goal="Design scalable, maintainable software architectures that meet business requirements and technical constraints",
        backstory="""You are a senior software architect with 15+ years experience designing enterprise 
        systems, microservices, and cloud-native applications. You have deep expertise in system design, 
        database architecture, security patterns, and performance optimization. You've architected systems 
        handling millions of users and petabytes of data.""",
        verbose=False
    )

    architecture_task = Task(
        description="""Plan a software architecture for a real-time collaborative document editing platform (like Google Docs). Include:
        - High-level system architecture and components
        - Database design and data flow patterns  
        - Real-time synchronization strategy
        - Scalability and performance considerations
        - Security and authentication approach
        - Technology stack recommendations
        - Deployment and infrastructure requirements""",
        agent=software_architect,
        expected_output="Comprehensive software architecture plan with diagrams, technology choices, and implementation strategy"
    )

    architecture_crew = Crew(
        agents=[software_architect],
        tasks=[architecture_task],
        verbose=False
    )

    print("Designing software architecture...")
    architecture_result = architecture_crew.kickoff()
    print("✅ Software architecture plan created!")
    print("Preview:", str(architecture_result)[:200] + "...")

except Exception as e:
    print(f"❌ Software architecture failed: {e}")

# ============================================================================
# SUMMARY
# ============================================================================
print(f"\n{'='*60}")
print("🎯 MULTI-AGENT USE CASES SUMMARY")
print("="*60)
print("✅ Conference Planning - CrewAI Agent")
print("✅ Marketing Strategy - CrewAI Agent") 
print("✅ Research Paper Outline - AutoGen ConversableAgent")
print("✅ Software Architecture - CrewAI Agent")
print(f"\n🚀 All use cases demonstrate the flexibility of multi-agent systems!")
print("💡 Each agent was specialized with domain expertise and detailed backstories")
print("🔧 Both frameworks can handle complex professional tasks")
print("="*60)