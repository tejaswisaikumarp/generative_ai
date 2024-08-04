**Neo4j** is a graph database. known for its **scalability and performance**. It offers a powerful query language called **Cypher**, simplifying graph traversal and querying.

Knowledge graph: It is a semantic network. A network of real-world entities
E.g.: New Delhi is the capital of India
India and New Delhi are the nodes (2). The type of the nodes is object.
The relationship between these nodes is ‘capital’.

**Question: How are the nodes created?**
**Answer: The technique is “Named Entity Recognition”.**

**Application:**
Financial institutions and insurance companies use Neo4j to detect fraudulent activities by analyzing patterns and relationships in transactions. By identifying unusual patterns and connections between entities, Neo4j helps in spotting fraud early

**Tech stack used:** 
Langchain, langchain-community, langchain_experimental langchain-groq
GraphDB: Neo4j (https://neo4j.com/cloud/platform/aura-graph-database/)
Groq Model: Gemma2-9b-It (https://console.groq.com/playground)

**Technical Architecture**
Text ----> Document------> Graph data -----> CypherQuery with result
**LLMGraphTransformer:** Extracting graph data from text enables the transformation of unstructured information into structured formats
Finally store it to Ne04j database 
**GraphCypherQAChain** library is used to convert the query to cypherquery. When it hits the database, the result will be generated.
