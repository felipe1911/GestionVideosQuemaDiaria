class DisplayRecommendations:
    def __init__(self, recommendations):
        self.recommendations = recommendations

    def display(self):
        for result in self.recommendations:
            print(f"Curso: {result['title']}, Puntaje de similitud: {result['similarity_score']} %")
            print(f"Etiquetas comunes: {', '.join(result['common_tags'])}")
            print("\n")