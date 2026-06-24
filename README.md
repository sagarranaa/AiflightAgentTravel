# ✈️ AI Travel Planner - Multi-Agent System using LangGraph

An AI-powered Travel Planning application built using **Python, LangGraph, Groq LLM, Pydantic, and Streamlit**.

This project demonstrates how multiple AI agents can collaborate through a shared state to plan and optimize a travel experience. Each agent has a specialized responsibility, and LangGraph manages the workflow between them.

---

## 🚀 Features

- 🤖 Multi-Agent Architecture
- 🔄 LangGraph-based Agent Workflow
- 📦 Shared State Management using Pydantic
- ✈️ Flight Planning Agent
- 🏨 Hotel Selection Agent
- 💰 Budget Calculation Agent
- 🔁 Cost Optimization Agent with Looping
- 🧠 LLM Integration using Groq
- 🖥️ Interactive Streamlit Frontend
- ⚡ Fast Python dependency management using UV

---

## 🏗️ System Architecture

```
                User Input
                     |
                     v
            Streamlit Frontend
                     |
                     v
              TravelState
            (Shared State)
                     |
                     v
                LangGraph
                     |
        --------------------------------
        |              |               |
        v              v               v
 Flight Agent    Hotel Agent    Budget Agent
        |              |               |
        --------------------------------
                     |
          Is Trip Within Budget?
                     |
            Yes               No
             |                |
             v                v
       Final Result     Optimizer Agent
                              |
                              |
                              v
                    Find Cheaper Options
                              |
                              |
                              v
                        Budget Agent
                           (Loop)
```

---

## 🧩 How It Works

### 1. User provides travel details

The user enters:

- Destination
- Number of days
- Travel budget

Example:

```json
{
  "destination": "Goa",
  "days": 2,
  "budget": 10000
}
```

---

### 2. Flight Agent

The Flight Agent searches and selects a suitable flight option.

Example Output:

```json
{
  "airline": "Indigo",
  "price": 4500
}
```

---

### 3. Hotel Agent

The Hotel Agent selects accommodation based on the trip details.

Example Output:

```json
{
  "name": "Sea View Resort",
  "price": 7000
}
```

---

### 4. Budget Agent

Calculates:

- Flight cost
- Hotel cost
- Total trip cost

Checks whether the trip is inside the user's budget.

---

### 5. Optimizer Agent

If the trip exceeds the budget, the optimizer agent reduces costs and sends the updated state back for budget validation.

This demonstrates LangGraph's **conditional routing and looping capability**.

---

## 📁 Project Structure

```
ai-travel-agent/
│
├── app/
│   │
│   ├── agents/
│   │   ├── flight_agent.py
│   │   ├── hotel_agent.py
│   │   ├── budget_agent.py
│   │   └── optimizer_agent.py
│   │
│   ├── graph/
│   │   └── travel_graph.py
│   │
│   ├── llm/
│   │   └── client.py
│   │
│   ├── parsers/
│   │   └── trip_parser.py
│   │
│   ├── schemas/
│   │   └── trip.py
│   │
│   └── state/
│       └── travel_state.py
│
├── frontend/
│   └── main.py
│
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python | Core Backend Development |
| LangGraph | Multi-Agent Workflow Management |
| Groq LLM | AI Reasoning and Language Model |
| Pydantic | Data Validation & State Management |
| Streamlit | Frontend Interface |
| UV | Python Package & Environment Management |

---

## 🔄 LangGraph Workflow Concepts Used

| Concept | Usage in Project |
|----------|-----------------|
| State | Stores trip information shared between agents |
| Node | Flight, Hotel, Budget, and Optimizer Agents |
| Edge | Controls movement between agents |
| Conditional Edge | Checks whether budget is exceeded |
| Loop | Runs Optimizer until budget conditions are satisfied |
| Agent Collaboration | Agents communicate using shared state |

---

## ▶️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ai-travel-agent
```

### 2. Create Environment

```bash
uv sync
```

### 3. Run Backend

```bash
uv run main.py
```

### 4. Run Streamlit Frontend

```bash
uv run streamlit run frontend/main.py
```

---

## 📸 Demo

### User Input

```
Destination: Delhi
Days: 10
Budget: ₹100000
```

### AI Travel Plan

```
✈️ Flight:
Indigo - ₹4500

🏨 Hotel:
Sea View Resort - ₹7000

💰 Total Cost:
₹11500

✅ Trip is within budget
```

---

## 🧠 Key Learnings

Through this project, I explored:

- Designing Multi-Agent AI Systems
- LangGraph State Management
- Agent-to-Agent Communication
- Conditional Workflows
- Looping in Agent Systems
- Structured Data Validation with Pydantic
- Building AI Interfaces with Streamlit
- Managing Python Projects using UV

---

## 🚀 Future Improvements

This project currently uses mock flight and hotel data for learning purposes.

Production-level improvements can include:

- Real Flight API integration (Amadeus, Skyscanner)
- Real Hotel Booking APIs
- Live price comparison
- LLM-powered decision-making agents
- User preference memory
- Database integration
- Authentication system
- Cloud deployment
- Monitoring and logging

---

## 🎯 Project Goal

The purpose of this project was to understand how real-world AI agent systems are designed.

The focus was on learning:

- How multiple agents work together
- How LangGraph manages workflows
- How agents share and update a common state
- How conditional execution and loops are implemented

The current architecture provides a strong foundation for building production-ready AI applications.

---

## 👨‍💻 Author

**Sagar Rana**

Generative AI, LangGraph, and Multi-Agent Systems 🚀

---

⭐ If you found this project interesting, feel free to give it a star and connect with me!
