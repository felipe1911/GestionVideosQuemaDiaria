
from recomend_courses import RecommendCourses
from display_recomendations import DisplayRecommendations

def interface_recommend_videos(user):
    recommendation_engine = RecommendCourses(user)
    recommendation_engine.find_recommendations()
    display_engine = DisplayRecommendations(recommendation_engine.similarity_results)
    display_engine.display()