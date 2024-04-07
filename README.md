# Evita - Eviction based ChatGPT Assistant

# Goal

Create a chatbot to assist tenants going through eviction, so they do not have to wait on hold to speak to an advocate.

# Deliverables

* [EVITA] - development version of the Chatbot, hosted on Vercel
* [Presentation about EVITA]: https://docs.google.com/presentation/d/1dcdziyrvhOPOpAoQDHUvN53njSDLvt8QxWQ1Xukuuc4/edit?usp=sharing

# Team

* Sri Sudersan Thopey Ganesh
* Zakir Jiwani
* Jerome Barnes
* Jonathan Pyle from [Philadelphia Legal Assistance]

# What is the overall mission and objective of the project?

Over 21,000 tenants in Philadelphia last year faced the prospect of being evicted from their rental unit. In order to get help to avoid eviction, they had to call legal assistance hotlines that are understaffed due to lack of funding. Many callers could only get through to an operator after waiting on hold for a long time. Ideally, the City would provide more funding for assistance to tenants. However, that is unlikely to happen.

Has AI technology improved to the point where a chatbot (perhaps a voice chatbot) could provide meaningful assistance to tenants facing eviction? Perhaps not, but we will not know unless we try to create one, and that is the goal of this project.

# What is your organization’s mission? Why do you care about this idea?

[Philadelphia Legal Assistance](https://github.com/philadelphialegalassistance) is a non-profit organization that provides free legal assistance in civil matters to low-income Philadelphia residents. Its mission is to enforce and protect the rights of individuals and families by providing accessible, creative and high-quality legal assistance and working collaboratively for systemic change. This idea matters because we should make sure that low-income people who have a pressing legal need can get meaningful assistance quickly and conveniently.

# What are the top three goals of the project?

1. Test whether a chatbot (ChatGPT or another Large Language Model (LLM)) can provide adequate answers to questions about the eviction process in Philadelphia.
2. Test whether a chatbot can determine a user's current status in the eviction process by asking questions of the user.
3. Test whether a chatbot can, by having an open-ended conversation with a user, schedule the user for an appointment from a list of available appointments.

# Who are the top target beneficiaries (users, stakeholders, etc) of the project? What do you hope they gain from the value your project delivers?

The goal of the project is not necessarily to put a chatbot into production. The primary beneficiaries are legal assistance providers and government officials who will be better informed about the potential benefits and risks of providing service to low-income people through an LLM-powered automated system.

# Project Scope

We set out to develop a chatbot that is educated in Philadelphia-specific eviction facts and that can carry on a conversation with a tenant who is facing eviction. We also worked on a number of ChatGPT-based automation features, which we have not yet had time to integrate into the final chatbot. The source code for these is in the `prototypes` branch of the repository.

# Are there other dependencies, resources, or partners you anticipate using or needing in order to deliver the project?

Philadelphia Legal Assistance (PLA) has expertise on the Eviction Diversion Program, which is the first stage of the eviction process in Philadelphia. Later on, we may tap into the expertise of the advocates at Community Legal Services.

# Who are the key contacts and stakeholders? What are their roles, involvement expectations and skill sets?

The primary point of contact is Jonathan Pyle from Philadelphia Legal Assistance. He can be reached at 215-391-9686, jhpyle@gmail.com, or through GitHub at @jhpyle.

# Target Delivery Date - and any particular drivers of that date

There is no target delivery date. The goal of the project is to learn and ultimately to educate the community of service providers about the benefits and risks of delivering services to low-income people through a chatbot.

# Data for this Project

The main "data" for the project is not data per se, but legal information. Jonathan Pyle (@jhpyle) provided written materials containing the legal knowledge that the chatbot will need to know in order to provide helpful information to tenants. Zakir consolidated the materials into a prompt.

Other data sources included:
- The code violations dataset on opendataphilly.org.
- The eviction court dockets, available through an API provided by Philadelphia Legal Assistance.
- Google Calendar, through its API.

[Presentation about EVITA]: https://docs.google.com/presentation/d/1dcdziyrvhOPOpAoQDHUvN53njSDLvt8QxWQ1Xukuuc4/edit?usp=sharing
[Philadelphia Legal Assistance]: https://philalegal.org