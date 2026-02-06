# Testing Remote MCP Server

## 📌 Overview
This repository demonstrates a **proof-of-concept implementation of a remote MCP (Model Context Protocol) server**, created to understand MCP server architecture, tool exposure, and cloud deployment workflows.  
The project focuses on **building, testing, and deploying an MCP server to MCP Cloud**, validating end-to-end connectivity and tool invocation.

## 🎯 Objective
- Learn how MCP servers are structured
- Implement a basic MCP server
- Deploy the server to MCP Cloud
- Verify remote tool accessibility and server stability

## 🧠 What is MCP?
**Model Context Protocol (MCP)** enables AI agents to securely interact with external tools, APIs, and services through standardized servers.  
This project explores MCP from a **developer and systems integration perspective**.

## 🏗️ Project Scope
- MCP server initialization
- Tool registration and exposure
- Cloud deployment configuration
- Remote server testing

This repository is **experimental** and intended for learning and validation purposes rather than production use.

## 🛠️ Tech Stack
- **Python**
- **MCP SDK**
- **MCP Cloud**
- **Async programming (asyncio)**

## 📂 Repository Structure
esting-Remote-MCP/
├── server.py # MCP server implementation
├── requirements.txt
├── README.md


## ⚙️ Setup & Installation

1. Clone the repository
```bash
git clone https://github.com/PrasannaMadiwar/Testing-Remote-MCP.git
cd Testing-Remote-MCP

2.  Install dependencies
pip install -r requirements.txt

3. Run the MCP server locally
python server.py
```

## ☁️ Deployment

The MCP server was deployed to MCP Cloud

Deployment validates:

Server registration

Remote accessibility

Tool exposure correctness

## ✅ Key Learnings

MCP server lifecycle

Remote AI tool serving

Cloud-based AI infrastructure basics

Debugging MCP communication issues

## 🚀 Future Improvements

Add authenticated tool access

Implement real-world AI/ML utilities

Logging and monitoring support

Production-grade deployment setup

## 📖 References

MCP Documentation

MCP Cloud Deployment Guides

## 👤 Author

Prasanna Madiwar
AI/ML Engineering Intern Aspirant
GitHub: https://github.com/PrasannaMadiwar



