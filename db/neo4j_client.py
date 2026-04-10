from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "neo4j123"   # <-- use your actual password

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))