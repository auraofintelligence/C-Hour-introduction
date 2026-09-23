## Sovereign Space Builder

## Part 1 of Full System & Implementation

0. Front Matter

0.1 Executive Summary

0.2 Design Principles & Ethos

0.3 Scope & Non-Goals

0.4 Audience & Roles

0.5 Definitions, Abbreviations, Glossary

1. Vision & Use Cases

1.1 Narrative Vision (Home → Planetary Ark)

1.2 Primary Use Cases

1.3 Personas

1.4 Success Metrics

2. System Overview

2.1 High-Level Architecture (Client, Edge, Mesh, Cloud-optional)

2.2 Core Subsystems

2.3 Data Flow & Event Bus

2.4 Trust & Consent Model

3. Game Design & UX

3.1 Player Loop (Spawn→Scan, Collect→Design, Sim→Do, Review→Share)

3.2 Memory-Palace UX

3.3 Progression & Rewards

3.4 Accessibility & Low-Tech Modes

3.5 Internationalisation & Cultural Modes

13. Data Model & APIs

13.4 Ark Objects

13.5 Event Model

21. Appendices

F. Data Schemas (full JSON)

G. API Reference (Events)

Works cited

## 0. Front Matter

## 0.1 Executive Summary

This document outlines the vision, architecture, and implementation plan for the Sovereign Space Builder, a gamified digital twin system designed for personal and environmental regeneration. The system begins as a standalone, offline-first application (a "Sovereign Node") that allows an individual to map their self and their immediate environment ("place"). It then scales fractally, connecting with nearby nodes to form community meshes and eventually contributing to a decentralised, planetary-scale knowledge commons-the "Fractal Ark." The core of the system is a dual digital twin: a Human Digital Twin (HDT) modelling the user's health and a corresponding Environmental Digital Twin (EDT) modelling their living space. Through a gamified loop rooted in permaculture principles, users are guided to observe, design, simulate, and build regenerative systems for their body and their environment.

Technologically, the system is built on a foundation of decentralised principles: peer-to-peer networking, offline-first data synchronisation using CRDTs, and user-owned identity via Decentralised Identifiers (DIDs) and Verifiable Credentials (VCs). Governance is fractal, with DAOs operating at the neighborhood, bioregion, and planetary levels. This architecture ensures data sovereignty, resilience, and scalability, creating a tool that is not only powerful but also ethical and community-owned by design.

The vision extends from personal well-being in a home garden to advanced applications in automated agriculture, robotics, and off-world habitats, all contributing to a shared, verifiable, and permanent library of life and regenerative practice.

## 0.2 Design Principles & Ethos

The system is guided by a non-negotiable ethos of Sovereignty and Joyful, Responsible Abundance. This ethos is expressed through the following core design principles:

- Sovereignty (Self-Rule): Every user owns and controls their data, identity, and the physical systems they build. The architecture is designed to empower the individual and the community, not to extract from them. This aligns with the permaculture ethic of People Care .
- Regeneration (Active Healing): The system's goal is not merely to sustain but to actively improve the health and vitality of both the user and their ecosystem. It is a shift from "doing less harm" to becoming an agent of positive change. This embodies the permaculture ethic of Earth Care .
- Fractal Scaling (Pattern Replication): The system's logic is designed to work at every scale, from a single room to the entire planet. The patterns of data, governance, and interaction at the individual level are replicated at the community and bioregional levels, ensuring coherence and resilience.
- Decentralisation by Default: The system avoids single points of failure and control. Data, computation, and governance are distributed across the network of users, creating a resilient, peer-to-peer architecture.
- Offline-First: The application could be fully functional without an internet connection. Data is stored locally, and synchronisation with the network happens opportunistically. This ensures utility in remote, disconnected, or disaster-prone environments.
- Data Dignity: The system respects the user's right to privacy and consent. Data sharing
- is explicit, purpose-bound, and revocable. It incorporates principles of Indigenous data sovereignty, allowing for local guardianship and tiered access to knowledge.
- Interoperability & Openness: The system is built on open standards and schemas to prevent vendor lock-in and encourage a rich ecosystem of compatible tools and services.
- Joyful, Responsible Abundance: The user experience is designed to be engaging, empowering, and fun. It celebrates the abundance that comes from regenerative practice while upholding the permaculture ethic of Fair Share -setting limits and redistributing surplus for the good of the commons.

## 0.3 Scope & Non-Goals

## In Scope:

- A cross-platform application (mobile, desktop) for individual users.
- Tools for mapping physical spaces (manual, AR-assisted).
- A digital twin system for modelling personal health (HDT) and environmental systems (EDT).
- A gamified user experience based on a permaculture design loop.
- A catalogue of modular building systems (e.g., hydroponic towers, composters).
- A simulation engine for modelling growth, resource use, and system resilience.
- An offline-first, peer-to-peer data synchronisation mechanism.
- A decentralised identity and verifiable claims system.
- A framework for fractal, multi-level DAO-based governance.
- Integration points for a future robotics and automation layer.
- Specialised modes for off-world habitat design and operation.

## Non-Goals:

- Centralised Data Hosting: The system will not operate a central cloud server for user data storage. All primary data resides on user devices.
- Manufacturing Physical Hardware: The platform will provide open-source blueprints and control software for modules (e.g., towers, robots) but will not manufacture the hardware itself.
- Token-as-Speculation: While the system uses internal tokens for governance and incentives (C-Hours), it is not designed as a financial speculation platform.
- Replacing Professional Medical Advice: The Human Digital Twin is a tool for personal insight and well-being, not a diagnostic medical device. It is not a substitute for professional medical care.
- Top-Down Control: The Planetary Stewards (L3) do not have control over lower-level DAOs; their role is to maintain standards and protocols for interoperability.

## 0.4 Audience & Roles

- Player: The primary user. An individual using the system to map their space, track their well-being, and build regenerative systems. They interact with the game loop, complete missions, and contribute data to the Ark.
- Builder: A user who fabricates, installs, or maintains physical modules (towers, composters, robots) based on the system's open-source designs.
- Developer: An engineer or designer who contributes to the open-source codebase of the application, develops new modules, or builds third-party tools that integrate with the system's APIs.
- Researcher: A scientist or academic who uses anonymised, aggregated data from the Fractal Ark (with appropriate permissions from the governing DAOs) to study ecological patterns, climate resilience, or community health.
- Custodian: An individual or group (e.g., an Indigenous community, a bioregional council) entrusted with the guardianship of specific knowledge or data within the Ark. They define and enforce access policies for sensitive information.

## 0.5 Definitions, Abbreviations, Glossary

- Ark: The decentralised, planetary-scale knowledge commons containing all user-contributed data.
- CID: Content Identifier. A unique hash derived from the content of a piece of data, used in systems like IPFS.
- CRDT: Conflict-free Replicated Data Type. A data structure that allows for concurrent edits on multiple devices to be merged automatically without conflicts.
- DAO: Decentralised Autonomous Organisation. A member-owned community without centralised leadership, governed by rules encoded on a blockchain.
- DID: Decentralised Identifier. A new type of identifier that enables verifiable, decentralised digital identity, controlled by the user.
- EDT: Environmental Digital Twin. A virtual replica of the user's physical environment.
- HDT: Human Digital Twin. A virtual replica of the user's physical, physiological, and psychological state.
- IPFS: InterPlanetary File System. A peer-to-peer protocol for storing and sharing content-addressed data.
- L0, L1, L2, L3: Levels of the Fractal Topology (Home, Neighbour, Bioregion, Planetary).
- Permaculture: A design philosophy for creating sustainable human environments by mimicking patterns found in nature.
- VC: Verifiable Credential. A tamper-proof digital credential that can be cryptographically verified.

## 1. Vision & Use Cases

## 1.1 Narrative Vision (Home → Planetary Ark)

The journey begins with a single person, Alex, in their small urban apartment. Feeling disconnected, Alex uses the Sovereign Space Builder app to map their balcony. The app guides them through a "Scout" mission, using their phone's camera to identify the few hardy plants growing there. This is L0: The Home Cell .

Alex then builds their Human Digital Twin, connecting their smartwatch and answering gamified psychological surveys. The system reveals a link between their afternoon energy slumps and the poor air quality near their window. A "Mission" is generated: "Build a Green Lung." Alex uses the Build System to design a small hydroponic tower, simulating its growth in the Sim environment before ordering the parts.

As Alex's tower thrives, they start generating a small surplus of basil. The app alerts them to the L1: Neighbour Mesh . They connect with a neighbor, Maria, and trade their basil for some of her sourdough starter. The mesh network shares anonymised data-not their personal details, but the learning that this basil variety grows well in their building's microclimate.

Months later, their entire building has formed a mesh. Their collective data on water usage, pest sightings, and successful plant guilds flows up as an anonymised summary to the L2:

Bioregion Guild . This guild, covering their entire watershed, uses this data to refine its "Pattern Packs"-templates for resilient urban gardens tuned to their specific climate.

Years pass. Alex's single tower has become a network of thousands. The data from their bioregion, and hundreds of others, has been verified and added to the L3: Planetary regenerative know-how. A researcher in another hemisphere, designing a mission for a Martian

Commons . This is the Fractal Ark : a living, breathing, user-built library of Earth's biology and habitat, downloads a "Drought-Resistant Guild" pattern from the Ark-a pattern whose wisdom began with Alex's single basil plant. From a single room to another world, the system has scaled, sharing wisdom without sacrificing sovereignty.

## 1.2 Primary Use Cases

- Room: A student in a dorm uses the system to build a microgreens rack and a small mushroom fruiting chamber, optimising their nutrition and air quality in a tiny space.
- Yard: A suburban family transforms their lawn into a permaculture food forest, using the Sim engine to plan guilds and the Ark to identify native pollinator-friendly plants. They use the Neighbour Mesh to share surplus produce and organise tool-sharing.
- Farm: A small-scale farmer uses the system for advanced crop planning, soil health monitoring, and integrated pest management. They use the robotics layer to automate planting and harvesting, and contribute detailed yield data to the Bioregion Guild.
- Off-World Base: An astronaut on a lunar base uses the system to manage a closed-loop life support system. They run advanced shock scenarios in the Sim engine ("What if the water reclaimer fails?") and use the robotics layer for autonomous greenhouse operations, all while drawing on the Ark's vast library of terrestrial agricultural knowledge.

## 1.3 Personas

- The Prepper (Zara): Zara is focused on resilience and self-sufficiency. She uses the system to maximise food and medicine production in her off-grid homestead. She values the offline-first architecture and the disaster playbook features.
- The Elder (Kenji): Kenji is a keeper of traditional ecological knowledge. He uses the system as a Custodian , mapping culturally significant plants and practices. He uses the tiered access controls to ensure this knowledge is shared appropriately, creating "in-place only" digital licenses.
- The Educator (Maria): Maria is a high school science teacher. She uses the system as a curriculum tool, creating "Biome Codex" quests for her students to map the biodiversity of the school grounds and local park.
- The Astronaut (Dr. Aris): Aris is the life-support systems specialist on a Mars mission. He is the ultimate power user, relying on the Twin, Sim, and Robotics subsystems to ensure the survival of his crew. He is also a key contributor to the Ark, sharing novel data on extremophile agriculture.
- The Community Gardener (Leo): Leo manages a shared garden plot in a dense city. He uses the L1 Neighbour Mesh DAO to coordinate planting schedules, manage the tool library, and route surplus food to a local shelter.

## 1.4 Success Metrics

- Food %: Percentage of a user's or community's caloric needs met by their own production.
- Medicine %: Percentage of basic first-aid and wellness needs met by homegrown medicinal plants.
- Resilience %: A composite score from the Sim engine, measuring the system's ability to withstand shocks (e.g., drought, power outage, pest outbreak) and maintain yield.
- Learning Rate: The speed at which a user completes "Codex" pages and masters new skills (e.g., composting, seed saving).
- Sharing Index: A measure of a user's or mesh's contribution to the commons, tracked via C-Hours earned and surplus routed.
- Biodiversity Score: A calculated index based on the number and diversity of species (plant, animal, insect) cataloged in the user's EDT.

## 2. System Overview

## 2.1 High-Level Architecture (Client, Edge, Mesh, Cloud-optional)

The system is a decentralised, peer-to-peer application with four logical layers of operation.

1. Client (The Sovereign Node): This is the application running on the user's device (phone, laptop). It is a complete, self-contained software stack that is fully functional offline. It stores the user's data, runs the digital twin and simulation models, and hosts the user interface.
2. Edge (Home Server - Optional): For power users (e.g., farms, off-world bases), an optional edge node can be set up on a local server (like a Raspberry Pi). This node acts as a persistent hub for the Home Cell (L0), managing the robotics fleet, handling more intensive simulations, and providing a stable connection point for the local mesh network.
3. Mesh (Peer-to-Peer Network): When online, the client application discovers and connects directly to other peers on the local network (LAN) and the wider internet. This peer-to-peer network is used for data synchronisation, federated learning, and DAO governance without relying on a central server.
4. Cloud-Optional (Replication & Discovery Hubs): The system does not require the cloud for core functionality. However, optional, community-run "Replication Hubs" can be used to pin important data (like Bioregion Pattern Packs) for higher availability. A lightweight cloud service may also be used as a bootstrap server to help peers discover each other initially.

## 2.2 Core Subsystems

- Twin: The core modelling engine. Manages the Human Digital Twin (HDT) and Environmental Digital Twin (EDT). It ingests sensor data, user logs, and assessment results to maintain a real-time virtual representation of the self-and-place system.
- Deck: The user's personal knowledge library. It functions as a collection of digital "cards"-photos, book scans, notes, web clips-that are tagged, linked, and anchored to specific places or objects in the Twin.
- Build: The design and crafting interface. Users browse a catalogue of open-source modules (beds, towers, etc.) and assemble them into systems within their digital twin. It includes a feasibility engine that checks for constraints (sun, water, skill).
- Sim: The predictive simulation engine. It takes the state of the Twin and the designs from the Build system and runs scenarios over time. It models plant growth, resource consumption, pest outbreaks, and system resilience against shocks.
- Missions: The gamification and operations engine. It analyses the delta between the current state of the Twin and the user's goals, generating a dynamic queue of tasks ("Missions" and "Quests") presented in Kanban and calendar views.
- Robots: The automation and fleet management layer. It provides the software interface for controlling and coordinating a fleet of heterogeneous robots (growers, drones, kitchen assistants) based on routines and mission tasks.
- Ark: The decentralised commons and governance layer. It manages the peer-to-peer synchronisation of data, the verification of claims, the workflow for graduating knowledge into the "Halls of Wisdom," and the operation of the fractal DAOs.

## 2.3 Data Flow & Event Bus

The system operates on an event-driven, pub/sub model.

1. Data Capture: A user performs an action (e.g., takes a photo of a plant, logs a meal, completes a harvest). This generates a new data object.
2. Local Commit: The object is structured as a CRDT and committed to the user's local, offline-first database. The UI updates immediately.
3. Content Addressing: The object is hashed, creating a unique Content Identifier (CID) .
4. Sync Gossip: When a network connection is available, the user's node "gossips" with its peers, advertising the CIDs of the new objects it has.
5. Peer Request: Peers that don't have these objects request them by their CID.
6. CRDT Merge: The receiving peer merges the new CRDT object into its own local database. Because CRDTs are used, this merge is mathematically intended to be conflict-free and eventually consistent.
7. Ark Publication (Optional): If the user chooses to publish the object to a higher level (e.g., L1 Mesh), a "publish" event is signed with their DID and broadcast to the relevant DAO. This event contains the CID of the data bundle (e.g., a "Season Pack").

## 2.4 Trust & Consent Model

The trust model is zero-trust and user-centric, built on W3C standards.

- Identity: Each Home Cell (L0) has a unique Decentralised Identifier (DID) . This DID is the root of the user's identity and is controlled by their cryptographic keys, not by a central server. Humans can remain pseudonymous.
- Claims: Every observation, achievement, or piece of knowledge contributed to the Ark is signed as a Verifiable Credential (VC) . This allows any peer to cryptographically verify who made the claim and that it hasn't been tampered with, without needing to contact the original issuer.
- Consent & Access Control: Data sharing is governed by explicit, granular consent. When a user shares a "Season Pack" with their L1 Mesh, they are issuing a VC that grants the Mesh DAO's DID access to that specific data bundle. Access policies are encoded in smart contracts, allowing for complex rules like:
- Tiered Access: Public, community-only, or custodial knowledge.
- Location Fuzsing: Raw GPS data never leaves L0 by default. L1 sees a fuzsed location (e.g., a 1km hex grid), and L2 only sees the bioregion.
- Custodial Licenses: For culturally sensitive knowledge, access can be restricted to specific DID groups or require physical presence for viewing (in-place only).
- Revocation: A user can "tombstone" any shared data bundle at any time, broadcasting a signed revocation message that instructs all peers to mark the data as withdrawn.

## 3. Game Design & UX

## 3.1 Player Loop (Spawn→Scan, Collect→Design, Sim→Do, Review→Share)

The core gameplay is an iterative loop designed to be intuitive and motivating.

1. Spawn & Scan (Observe): The player "spawns" into their digital twin. Their first action is to scan their environment using their phone's camera (AR) or manual tools. This populates the EDT and unlocks pages in their "Biome Codex."
2. Collect & Design (Analyse & Design): The player collects data (biometric, environmental) and knowledge (from their Deck). The system presents "Insight Puzzles" that connect disparate data points. The player then uses the Build System to design solutions, crafting new systems from a catalogue of modules.
3. Sim & Do (Simulate & Act): The player runs their design in the Sim engine to test its resilience and predict its yield. Once satisfied, the system generates a "Building Quest" in the Missions subsystem, breaking the real-world implementation into small, actionable steps.
4. Review & Share (Measure & Adapt): After building, the player completes "Measurement Quests" to update their Twin with real-world data, closing the feedback loop. They can then choose to synthesise their learnings into a "Guild Brief" and share it with their community mesh, earning reputation and C-Hours.

## 3.2 Memory-Palace UX

The primary user interface is a spatial "memory palace." Instead of navigating menus, the user navigates a 3D representation of their own space.

- Anchors: Key physical objects (a specific tree, a hydroponic tower, a compost bin) become persistent "anchors" in the digital twin.
- Hotspots: Users can attach information to these anchors. Tapping on the virtual representation of the apple tree reveals hotspots for its watering schedule, links to pruning guides in the Deck, a timeline of past harvest data, and photos of pest sightings.
- Place-based Recall: This UX leverages the human brain's natural strength for spatial memory. To find information about composting, the user doesn't search a file system; they simply "walk" to the compost bin in their digital twin and access the information anchored there.

## 3.3 Progression & Rewards

Motivation is driven by a multi-layered reward system that balances extrinsic and intrinsic drivers, based on Self-Determination Theory.

- XP & Levels (Competence): Players earn Experience Points (XP) for completing any action in the loop (scanning, building, harvesting). Gaining levels unlocks new modules in the Build catalogue, more advanced simulation scenarios, and new cosmetic options for their avatar/space.
- Badges & Taxon Ticks (Competence): Badges are awarded for significant achievements ("First Harvest," "Composter Level 3"). "Taxon Ticks" are earned for identifying and verifying new species for the Ark.
- Bounties & C-Hours (Autonomy & Relatedness): The community DAOs can post "Bounties" to fill knowledge gaps (e.g., "Map the flowering time of elderberries in this hex grid"). Completing these bounties earns C-Hours , a non-financial, time-bank token that can be exchanged for help from other community members.
- Halls of Wisdom (Relatedness & Mastery): The ultimate intrinsic reward is having a "Guild Brief" successfully peer-reviewed and merged into the Bioregion or Planetary Halls of Wisdom, establishing the player as a recognised expert and contributing to the global commons.

## 3.4 Accessibility & Low-Tech Modes

To ensure inclusivity, the system is designed to work across a spectrum of technological access.

- Printables: The system can generate printable QR codes that can be attached to physical objects. Scanning a QR code on a garden bed with a simple camera phone can bring up a basic web form for data entry.
- Offline Cards: For fully disconnected participation, the system can generate printable "Observation Cards" and "Harvest Log" sheets that can be filled out by hand and later entered into the system by a community member with a device.
- SMS/Photo Intake: A community mesh can set up a gateway number that allows members to submit observations by sending an SMS message or a photo, which is then parsed and added to the Ark by a bot.

## 3.5 Internationalisation & Cultural Modes

- I18n & L10n: The UI is fully internationalised (I18n) to support multiple languages. Community-driven localisation (L10n) efforts are incentivised through C-Hours.
- Cultural Protocols: The system's schemas and governance models are designed to be flexible. A Bioregion Guild can define its own "Custodial Licenses" and cultural protocols, which are enforced by smart contracts. This allows for the respectful handling of traditional ecological knowledge and other culturally sensitive information.

(Sections 4-21 and Appendices would continue in this detailed, structured format, referencing the provided table of contents and synthesising information from the research notes as demonstrated above.)

## 13. Data Model & APIs

(Excerpt to demonstrate schema and API generation)

## 13.4 Ark Objects

These are the core, interoperable data objects that form the payload of the Fractal Ark. They are designed to be extensible and are based on open standards where possible.

(See Appendix F for full JSON Schemas)

- Taxon: Represents a biological taxon. It extends the Darwin Core standard (dwc:) to include status and links.
- Place: A geographically defined area within a user's space. It includes geometry (based on GeoJSON) and privacy settings for location fuzsing.
- Observation: An instance of a Taxon observed at a Place at a specific time. It includes evidence (links to Media cards), confidence scores, and a list of attestations from peers.
- SeedLot: A record of a batch of seeds, including provenance, viability data, and access restrictions (public, mesh-only, custodial).
- Practice: A structured, how-to guide. This can be a recipe, a grow protocol, or a first-aid procedure. It includes steps, media links, and a license (e.g., CC-BY-SA or a custom Custodial License).
- SeasonPack: A content-addressed Merkle-DAG bundle that packages a collection of other Ark objects for sharing. It represents a snapshot of a user's space over a season.
- Reputation: A score attached to a specific claim (e.g., an Observation), not a person. It is built from a web of attestations.
- AccessPolicy: A machine-readable contract that defines the rules for accessing a specific object or set of objects, enforced by the DAO.

## 13.5 Event Model

The system's peer-to-peer communication is based on a simple set of signed events. (See Appendix G for API Reference)

- ark:publish: An event broadcast by a user to a DAO (e.g., L1 Mesh) to announce a new shareable bundle.
- Payload: { "object": "SeasonPack", "cid": "bafy...", "scope": "L1" }
- ark:attest: An event broadcast by a peer to attest to the validity of another user's claim.
- Payload: { "claimId": "cid\_of\_observation", "type": "peer\_review", "score": 0.9 }
- ark:adopt: An event logged by a user when they import a Pattern Pack from a higher-level commons into their own space.
- Payload: { "patternId": "cid\_of\_practice", "source": "L2:BioregionGuild" }
- ark:revoke: An event broadcast by a user to tombstone a previously published object.
- Payload: { "tombstoneFor": "cid\_of\_season\_pack", "reason": "Data entered in error." }
- crdt:merge: A low-level event handled by the sync protocol when a peer receives a new CRDT update from another peer.

## 21. Appendices

## F. Data Schemas (full JSON)

```
{ "ArkObject": {
```

```
"description": "Base object for all Ark entries.", "properties": { "id": { "type": "string", "description": "Content ID (CID) of the object." }, "type": { "enum": }, "created": { "type": "string", "format": "iso-date-time" }, "updated": { "type": "string", "format": "iso-date-time" }, "by": { "type": "string", "description": "DID of the creator." }, "sig": { "type": "string", "description": "JWS signature of the object." } }, "required": ["id", "type", "created", "updated", "by", "sig"] }, "Taxon": { "allOf": [{ "$ref": "#/ArkObject" }], "properties": { "dwc": { "description": "Fields based on Darwin Core standard.", "properties": { "scientificName": { "type": "string" }, "rank": { "type": "string" }, "vernacularNames": { "type": "array", "items": { "type": "string" } }, "links": { "properties": { "gbif": { "type": "string", "format": "uri" }, "tpl": { "type": "string", "format": "uri" } } } } }, "status": { "properties": { "iucn": { "enum": } } } } }, "Place": { "allOf": [{ "$ref": "#/ArkObject" }], "properties": { "name": { "type": "string" }, "kind": { "enum": ["bed", "tower", "pond", "tree", "wildpatch", "room"] }, "geom": { "description": "GeoJSON compliant geometry.", "properties": {
```

```
"type": { "enum": ["Polygon", "Point"] }, "coordinates": { "type": "array" } } }, "privacy": { "properties": { "loc": { "type": "string", "description": "Privacy-preserving location (e.g., hex grid ID)." }, "share": { "enum": ["L0", "L1", "L2", "L3"], "description": "Maximum topology level this object can be shared to." } } } } }, "Observation": { "allOf": [{ "$ref": "#/ArkObject" }], "properties": { "taxonId": { "type": "string", "description": "CID of a Taxon object." }, "placeId": { "type": "string", "description": "CID of a Place object." }, "when": { "type": "string", "format": "iso-date-time" }, "what": { "properties": { "stage": { "enum": ["seed", "seedling", "veg", "flower", "fruit", "dormant"] }, "phenophase": { "type": "array", "items": { "enum": ["leafOut", "flowerOpen", "ripe"] } } } }, "evidence": { "type": "array", "items": { "properties": { "kind": { "enum": ["photo", "audio", "log"] }, "cardId": { "type": "string", "description": "CID of a Media Card in the user's Deck." } } } }, "confidence": { "properties": { "self": { "type": "number", "minimum": 0, "maximum": 1 }, "peer": { "type": "number", "minimum": 0, "maximum": 1 }, "auto": { "type": "number", "minimum": 0, "maximum": 1 } } }, "attestations": {
```

```
"type": "array", "items": { "properties": { "by": { "type": "string", "description": "DID of the attester." }, "type": { "enum": ["peer_review", "expert_review", "robot_scan"] }, "score": { "type": "number", "minimum": 0, "maximum": 1 } } } } } }, "SeedLot": { "allOf": [{ "$ref": "#/ArkObject" }], "properties": { "taxonId": { "type": "string", "description": "CID of a Taxon object." }, "source": { "enum": ["garden", "wild", "swap", "commercial"] }, "harvest": { "type": "string", "format": "iso-date-time" }, "viability": { "type": "number", "minimum": 0, "maximum": 1 }, "qty": { "type": "integer" }, "provenance": { "properties": { "bioregion": { "type": "string" }, "custodian": { "type": "string", "description": "DID of the custodian." } } }, "restrictions": { "properties": { "share": { "enum": ["public", "mesh", "custodial"] } } } } }, "Recipe": { "allOf": [{ "$ref": "#/ArkObject" }], "properties": { "name": { "type": "string" }, "scope": { "enum": ["tower", "bed", "mushroom", "preserve"] }, "stages": { "type": "array", "items": { "properties": { "name": { "type": "string" }, "days": { "type": "integer" }, "targets": {
```

```
"properties": { "ec": { "type": "number" }, "ph": { "type": "number" } } } } } }, "haccp": { "properties": { "required": { "type": "boolean" } } } } }, "Practice": { "allOf": [{ "$ref": "#/ArkObject" }], "properties": { "kind": { "enum": ["grow", "medicine", "preserve", "build"] }, "title": { "type": "string" }, "steps": { "type": "array", "items": { "type": "string" } }, "media": { "type": "array", "items": { "type": "string", "description": "Array of CIDs of Media Cards." } }, "licenses": { "properties": { "use": { "enum": } } } } }, "SeasonPack": { "allOf": [{ "$ref": "#/ArkObject" }], "properties": { "index": { "properties": { "places": { "type": "array", "items": { "type": "string" } }, "observations": { "type": "array", "items": { "type": "string" } }, "seedLots": { "type": "array", "items": { "type": "string" } }, "recipes": { "type": "array", "items": { "type": "string" } }, "practices": { "type": "array", "items": { "type": "string" } } } }, "merkleRoot": { "type": "string", "description": "Merkle root
```

```
CID of the entire bundle." }, "scope": { "enum": ["L0", "L1", "L2", "L3"] } } }, "Reputation": { "allOf": [{ "$ref": "#/ArkObject" }], "properties": { "claimId": { "type": "string", "description": "CID of the claim being scored (e.g., an Observation)." }, "scores": { "properties": { "accuracy": { "type": "number" }, "safety": { "type": "number" }, "usefulness": { "type": "number" } } }, "justifications": { "type": "array", "items": { "type": "string", "description": "Array of CIDs of attestation objects." } } } }, "AccessPolicy": { "allOf": [{ "$ref": "#/ArkObject" }], "properties": { "rules": { "type": "array", "items": { "properties": { "objType": { "type": "string" }, "scope": { "type": "string" }, "allow": { "type": "array", "items": { "type": "string", "description": "Array of DIDs or DID groups." } }, "shareMax": { "enum": ["L0", "L1", "L2", "L3"] } } } } } } }
```

## G. API Reference (Events)

This section provides stubs for the primary API events an engineer would implement for the Ark subsystem. These are conceptual and would be implemented over a peer-to-peer transport layer.

## Event: ark:publish

- Description: Broadcasts a new data bundle (e.g., SeasonPack) to a specific governance scope (e.g., L1 Mesh DAO).
- Trigger: User explicitly chooses to share a synthesised pack from their Deck/Twin.
- Payload Schema:

```
{ "event": "ark:publish", "timestamp": "iso-date-time", "author": "did:user:...", "body": { "objectType": "SeasonPack", "cid": "bafy...", "scope": "L1" }, "signature": "jws_of_body" }
```

## Event: ark:attest

- Description: Broadcasts a peer review or verification of another user's claim.
- Trigger: User reviews an observation in their Neighbour Mesh and confirms its accuracy.
- Payload Schema:

```
{ "event": "ark:attest", "timestamp": "iso-date-time", "author": "did:user:...", "body": { "claimId": "cid_of_observation", "type": "peer_review", "score": 0.9, "comment": "Confirmed sighting. Clear photo." }, "signature": "jws_of_body" }
```

## Event: ark:adopt

- Description: Logs the action of a user importing a pattern from a higher-level commons into their local space.
- Trigger: User drags a "Bioregion Pattern" from the Build system into their personal Twin.
- Payload Schema:

```
{ "event": "ark:adopt", "timestamp": "iso-date-time", "author": "did:user:...", "body": { "patternId": "cid_of_practice_bundle", "source": "L2:BioregionGuild", "destinationPlaceId": "cid_of_local_place" }, "signature": "jws_of_body" }
```

## Event: ark:revoke

- Description: Broadcasts a tombstone message to invalidate a previously published object.
- Trigger: User deletes a shared SeasonPack or marks it as private.
- Payload Schema:

```
{ "event": "ark:revoke", "timestamp": "iso-date-time", "author": "did:user:...", "body": { "tombstoneFor": "cid_of_season_pack", "reason": "Data entered in error." }, "signature": "jws_of_body" }
```

## Works cited

1. Regenerative Systems through Permaculture - Number Analytics,

https://www.numberanalytics.com/blog/regenerative-systems-through-permaculture 2. Regenerative Systems Thinking → Term, https://lifestyle.sustainability-directory.com/term/regenerative-systems-thinking/ 3. Regenerative System Thinking → Term - Lifestyle → Sustainability Directory,

https://lifestyle.sustainability-directory.com/term/regenerative-system-thinking/ 4. Ethical Issues of Digital Twins for Personalized Health Care Service ..., https://pmc.ncbi.nlm.nih.gov/articles/PMC8844982/ 5. (PDF) Human Digital Twins in Personalized Healthcare: An ...,

https://www.researchgate.net/publication/389916943\_Human\_Digital\_Twins\_in\_Personalized\_H ealthcare\_An\_Overview\_and\_Future\_Perspectives 6. Behavior Change through Gamification -

Number Analytics, https://www.numberanalytics.com/blog/behavior-change-through-gamification
