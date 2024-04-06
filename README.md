<<<<<<< HEAD
# Idea Name

Create a chatbot to assist tenants going through eviction, so they do not have to wait on hold to speak to an advocate.

# Describe the idea. What is the overall mission and objective of the project? 

Over 21,000 tenants in Philadelphia last year faced the prospect of being evicted from their rental unit. In order to get help to avoid eviction, they had to call legal assistance hotlines that are understaffed due to lack of funding. Many callers could only get through to an operator after waiting on hold for a long time. Ideally, the City would provide more funding for assistance to tenants. However, that is unlikely to happen.

Has AI technology improved to the point where a chatbot (perhaps a voice chatbot) could provide meaningful assistance to tenants facing eviction? Perhaps not, but we will not know unless we try to create one, and that is the goal of this project.

# What is your organization’s mission? Why do you care about this idea? 

[Philadelphia Legal Assistance](https://github.com/philadelphialegalassistance) is a non-profit organization that provides free legal assistance in civil matters to low-income Philadelphia residents. Its mission is to enforce and protect the rights of individuals and families by providing accessible, creative and high-quality legal assistance and working collaboratively for systemic change. This idea matters because we should make sure that low-income people who have a pressing legal need can get meaningful assistance quickly and conveniently.

# Can you rank the top three goals of the project? 

1. Test whether a chatbot (ChatGPT or another Large Language Model (LLM)) can provide adequate answers to questions about the eviction process in Philadelphia.
2. Test whether a chatbot can determine a user's current status in the eviction process by asking questions of the user.
3. Test whether a chatbot can, by having an open-ended conversation with a user, schedule the user for an appointment from a list of available appointments.

# Who are the top target beneficiaries (users, stakeholders, etc) of the project? What do you hope they gain from the value your project delivers? 

The goal of the project is not necessarily to put a chatbot into production. The primary beneficiaries are legal assistance providers and government officials who will be better informed about the potential benefits and risks of providing service to low-income people through an LLM-powered automated system.

# Project Scope - Rank, to the best of your ability, what you hope to deliver with the project. At the very least, if you could choose to deliver only one feature, what would it be?

1. The minimum deliverable is a presentation containing what was learned. Legal services organizations do not have time to explore the capacity of LLMs, so whatever we learn through a process of experimentation will be extremely helpful to the organizations that serve tenants.
2. If more can be done, the scope can be expanded to include standalone "proofs of concept" for the separate pieces of the project: a) a prompt that educates ChatGPT about the correct advice to give a tenant in Philadelphia who is facing eviction; b) a prompt that instructs ChatGPT to ask questions to determine the tenant's current status in the eviction process; c) a prompt that instructs ChatGPT to schedule the user for an appointment from a list of available appointments.
3. If still more can be done, the above pieces can be integrated into a single web app or voice app.

# Are there other dependencies, resources, or partners you anticipate using or needing in order to deliver the project? 
Philadelphia Legal Assistance (PLA) has expertise on the Eviction Diversion Program, which is the first stage of the eviction process in Philadelphia. Later on, we may tap into the expertise of the advocates at Community Legal Services.

# Who are the key contacts and stakeholders? What are their roles, involvement expectations and skill sets? 
The primary point of contact is Jonathan Pyle from Philadelphia Legal Assistance. He can be reached at 215-391-9686, jhpyle@gmail.com, or through GitHub at @jhpyle. He is an attorney and also a coder. He is the developer of the guided interview platform [docassemble](https://github.com/jhpyle/docassemble). Jonathan will be at the hackathon all weekend to lead the team that works on this project.

# Target Delivery Date - and any particular drivers of that date
No target delivery date. The goal of the project is to learn.

# Anything else we should know? 
This project is open to people of any level of experience with technology. It is largely a "prompt engineering" project.

If you have never written a line of code in your life, you can sit down with ChatGPT, and go through a process of trying to incrementally improve its responses. This is really the core of the project. One of the really important parts of the process is to write down observations. Was the chatbot incorrect about something? Did it hallucinate facts that are untrue? Did it exhibit bias? These tasks do not require the participant to have any background knowledge.

If you are a coder, there are sticky coding issues to work on, such as using regular expressions to parse ChatGPT output, writing "glue code" between ChatGPT and APIs.

# Data for this Project
The main "data" for the project is not data per se, but legal information. Jonathan Pyle (@jhpyle) will provide written materials containing the legal knowledge that the chatbot will need to know in order to provide helpful information to tenants.

Jonathan can also provide an API for looking up an eviction case in Philadelphia Municipal Court based on a tenant's name and address and obtaining machine-readable information about the events in the case. In experiments, Jonathan found that ChatGPT is good at taking this data and explaining it to the user in conversational plain language. This could be refined further with appropriate prompt engineering.

For the appointment scheduling component of the project, Jonathan can provide an API interface for retrieving available appointments and scheduling an appointment. But if someone on the team wants to figure out how to do that in Python, that would be helpful. 
=======
# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh
>>>>>>> first-model
