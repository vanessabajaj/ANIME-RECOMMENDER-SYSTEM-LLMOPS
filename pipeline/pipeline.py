from src.vector_store import VectorStore
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException
logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self, persist_dir: str = "chroma-db"):
        try:
            logger.info("Initializing the Anime Recommendation Pipeline.")
            vector_builder = VectorStore(persist_directory=persist_dir)
            retriever = vector_builder.get_retriever()
            self.recommender = AnimeRecommender(
                retriever, api_key=GROQ_API_KEY, model_name=MODEL_NAME
            )
            logger.info("Pipeline initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing the pipeline: {e}")
            raise CustomException(f"Error initializing the pipeline: {e}")

    def recommend(self, user_query: str):
        try:
            logger.info(f"Received user query: {user_query}")
            recommendations = self.recommender.get_recommendations(user_query)
            logger.info("Recommendations generated successfully.")
            return recommendations
        except Exception as e:
            logger.error(f"Error generating recommendations: {e}")
            raise CustomException(f"Error generating recommendations: {e}")