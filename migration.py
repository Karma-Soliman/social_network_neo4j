import sqlite3
from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(uri, auth=(user, password))

#sql connection
sqlite_conn = sqlite3.connect("social_network.db")
sqlite_cursor = sqlite_conn.cursor()

#incomplete 