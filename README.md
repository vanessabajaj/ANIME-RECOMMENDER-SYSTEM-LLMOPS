# Anime Recommendation System

A lightweight local anime recommender that builds a Chroma vector store from an anime CSV and serves recommendations via a Streamlit UI backed by a ChatGroq LLM prompt. 
This repository contains a small data-pipeline, a vector store wrapper, and a Streamlit app to query the recommender.

Status:Development — pipeline and Streamlit app run locally (see Troubleshooting).

Contents:
- app/ — Streamlit frontend (app.py)
- pipeline/ — pipeline runner and build script (build_pipeline.py, pipeline.py)
- src/ — core modules: data_loader.py, vector_store.py, recommender.py, prompt_template.py
- data/ — raw and processed CSVs (anime_with_synopsis.csv, anime_processed.csv)
- chroma-db/ — persisted Chroma DB (created by pipeline)
- config/ — configuration (config.py)
- utils/ — logging and custom exceptions
