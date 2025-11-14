#!/usr/bin/env python3
"""
Enhanced CrewAI Flight Specialist Agent Demo
==========================================

This demonstrates a more detailed Agent configuration
with enhanced role, goal, and backstory.
"""

from crewai import Agent, Task, Crew

# Enhanced Flight Agent
flight_agent = Agent(
    role="Senior Flight Research Specialist",  # ← Modified - more specific
    goal="Find the most cost-effective and convenient flight options while analyzing pricing trends, route efficiency, and traveler preferences to deliver optimal booking recommendations",
    backstory="""You are a seasoned travel industry expert with over 15 years of experience in airline operations, 
    booking systems, and travel optimization. Your expertise includes:
    
    • Deep knowledge of airline pricing algorithms and fare classes
    • Understanding of route networks and hub-and-spoke systems  
    • Expertise in seasonal pricing trends and booking windows
    • Familiarity with airline partnerships, codeshare agreements, and alliances
    • Knowledge of baggage policies, seat selection, and ancillary fees
    • Experience with loyalty programs and elite status benefits
    
    You have successfully helped over 10,000 travelers find perfect flights by analyzing real-time data,
    understanding market dynamics, and providing strategic booking advice. You stay current with 
    industry changes, new routes, and emerging airlines to offer the most comprehensive recommendations.""",  # ← Extensive detail added
    verbose=True,
    allow_delegation=False
)

# Enhanced Task
flight_task = Task(
    description="""Research and analyze flight options from New York (JFK/LGA/EWR) to Reykjavik, Iceland (KEF) 
    for travel dates January 15-20, 2026. Provide:
    
    1. At least 3 different flight options with detailed pricing
    2. Analysis of direct vs connecting flights
    3. Recommendations on optimal booking timing
    4. Comparison of airline amenities and policies
    5. Tips for maximizing value (upgrades, loyalty points, etc.)
    
    Consider factors like flight duration, departure times, airline reliability, 
    and overall passenger experience in your recommendations.""",
    agent=flight_agent,
    expected_output="Comprehensive flight analysis with specific recommendations, pricing details, and booking strategy for NYC to Reykjavik travel"
)

if __name__ == "__main__":
    print("🛩️  Enhanced Flight Specialist Agent Demo")
    print("=" * 50)
    
    # Create and run crew
    crew = Crew(
        agents=[flight_agent], 
        tasks=[flight_task], 
        verbose=True, 
        process="sequential"
    )
    
    try:
        result = crew.kickoff()
        print("\n✅ Flight research completed!")
        print("="*50)
        print("RESULT:")
        print(result)
    except Exception as e:
        print(f"❌ Error: {e}")