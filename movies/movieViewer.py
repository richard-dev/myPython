import movies
import fresh_tomatoes

TOYSTORY = movies.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

# print(TOYSTORY.storyline)

AVATAR = movies.Movie("Avatar",
                      "A marine on an alien planet.",
                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# print(AVATAR.storyline)
# AVATAR.showTrailer()
SCHOOLOFROCK = movies.Movie("School of Rock",
                            "Using rock music to learn.",
                            "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                            "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

RATATOUILLE = movies.Movie("Ratatouille",
                           "A rat is a chef in Paris",
                           "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                           "https://www.youtube.com/watch?v=c3sBBRxDAqk")

MIDNIGHTINPARIS = movies.Movie("Midnight in Paris",
                               "Going back in time to meet authors.",
                               "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                               "https://www.youtube.com/watch?v=FAfR8omt-CY")   

HUNGERGAMES = movies.Movie("Hunger Games",
                           "A really real reality show.",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

MOVIES = [TOYSTORY, AVATAR, SCHOOLOFROCK, RATATOUILLE, MIDNIGHTINPARIS, HUNGERGAMES]

fresh_tomatoes.open_movies_page(MOVIES)
