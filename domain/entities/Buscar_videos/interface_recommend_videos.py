
from .recomend_courses import RecommendCourses
from .display_recomendations import DisplayRecommendations
from .load_data_comand import LoadDataCommand


def interface_recommend_videos(user):
    db_data = LoadDataCommand('domain\database\database_courses.json').execute()
    recommendation_engine = RecommendCourses(user, db_data)
    recommendation_engine.find_recommendations()
    display_engine = DisplayRecommendations(recommendation_engine.similarity_results)
    display_engine.display()