# Text Search and Retrieval Script

The Text Search and Retrieval Script is a Python script designed to perform text search and retrieval operations on a collection of documents. It supports both linear and inverted index-based search modes and offers additional features like stemming and stop-word removal.

## Features

- **Linear Search:** Search for a query text in a collection of documents using linear search. The script will return documents containing the query.

- **Inverted Index Search:** Perform more efficient searches using an inverted index. Retrieve documents that match a query.

- **Stemming:** Enable stemming to find variations of words (e.g., "running" matches "run"). It uses the Porter stemming algorithm.

- **Stop-Word Removal:** Optionally remove common stop words from the query to focus on meaningful keywords.

- **Query Language:** Use a simple query language to combine search terms using "&" for AND operations and "!" for NOT operations.
