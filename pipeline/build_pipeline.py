from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException
load_dotenv()
logger = get_logger(__name__)
def main():
    try:
        logger.info("Starting the data loading and vector store building process.")
        original_csv_path = "C:\\Users\\hp\\OneDrive\\Documents\\ANIMERECOMED_P1\\data\\anime_with_synopsis.csv"
        processed_csv_path = "C:\\Users\\hp\\OneDrive\\Documents\\ANIMERECOMED_P1\\data\\anime_processed.csv"
        
        loader = AnimeDataLoader(original_csv_path, processed_csv_path)
        processed_df = loader.load_and_process_data()
        vector_builder = VectorStoreBuilder(processed_csv_path, persist_dir="chroma-db")
        vector_builder.build_vector_store()
        logger.info("Data loading and vector store building process completed successfully.")   
    except Exception as e:
        logger.error(f"Error in data loading and vector store building process: {e}")
        raise CustomException(f"Error in data loading and vector store building process: {e}")      
if __name__ == "__main__":    main()    

    