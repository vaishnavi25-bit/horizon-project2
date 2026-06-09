import pandas as pd

movies = pd.read_csv("cleaned_movies.csv")

genre = input("Enter genre: ")
rating = float(input("Enter minimum rating: "))
year = int(input("Enter year: "))

filtered_movies = movies[
    (movies['Genre'].str.contains(genre, case=False, na=False)) &
    (movies['Rating'] >= rating) &
    (movies['Year'] == year)
]

recommendations = filtered_movies.sort_values(
    by='Rating',
    ascending=False
)

if recommendations.empty:
    print("No movies found matching your criteria.")
else:
    print("\nRecommended Movies:\n")
    print(recommendations[['Title', 'Genre', 'Rating', 'Year']].head(10))