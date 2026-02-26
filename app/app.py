import os, sys

# ensure project root is on sys.path when Streamlit changes cwd to \"app\"
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

# data_loader and vector_store imports are no longer used in the app directly
# from src.data_loader import AnimeDataLoader 
# from src.vector_store import VectorStoreBuilder
load_dotenv()
st.set_page_config(page_title="Anime Recommendation System", layout="wide")

@st.cache_resource
def get_pipeline():
    # cache the pipeline instance so it isn't rebuilt on every rerun
    try:
        with st.spinner("Loading and processing data..."):
            return AnimeRecommendationPipeline()
    except Exception as e:
        st.error(f"Error initializing pipeline: {e}")
        st.stop()

try:
    run_pipeline = get_pipeline()
except Exception as e:
    st.error(f"Failed to load pipeline: {e}")
    st.stop()

st.title("Anime Recommendation System")
query = st.text_input("Enter your anime preferences (e.g., genres, themes, etc.):")
if query:
    with st.spinner("Generating recommendations..."):
        recommendations = run_pipeline.recommend(query)
    st.subheader("Recommended Anime:")
    # recommendations is a single formatted string
    st.write(recommendations) 

# # Load and process data
# data_loader = DataLoader("anime_with_synopsis.csv", "anime_processed.csv")
# processed_data = data_loader.load_and_process()
    
# st.write("Building vector store...")
# vector_store_builder = VectorStoreBuilder("anime_processed.csv", "chroma-db")
# vector_store_builder.build_vector_store()
    
# st.write("Data loading and vector store building completed successfully.")  
# if __name__ == "__main__":    main()
