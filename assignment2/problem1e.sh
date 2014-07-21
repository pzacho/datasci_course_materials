#!/bin/sh
sqlite3 reuters.db < problem1e.sql | wc -l > big_documents.txt
