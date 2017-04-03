import media
import fresh_tomatoes

# Creating all the instances of Pixar movies
coco = media.Movie("Coco",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BNTEyMzE4Nzc0NV5BMl5BanBnXkFtZTgwMDEwOTk2MTI@._V1_SX674_CR0,0,674,999_AL_.jpg",
                   "https://www.youtube.com/watch?v=zNCz4mQzfEI")

cars = media.Movie("Cars 3",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc0NzU2OTYyN15BMl5BanBnXkFtZTgwMTkwOTg2MTI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                   "https://www.youtube.com/watch?v=E4K7JgPJ8-s")

up = media.Movie("Up",
                 "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk3NDE2NzI4NF5BMl5BanBnXkFtZTgwNzE1MzEyMTE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                 "https://www.youtube.com/watch?v=pkqzFUhGPJg")

finding_dory =  media.Movie("Finding Dory",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BNzg4MjM2NDQ4MV5BMl5BanBnXkFtZTgwMzk3MTgyODE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=JhvrQeY3doI")

inside_out = media.Movie("Inside Out",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BOTgxMDQwMDk0OF5BMl5BanBnXkFtZTgwNjU5OTg2NDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                         "https://www.youtube.com/watch?v=WIDYqBMFzfg")

good_dino = media.Movie("Good Dinosaur",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc5MTg2NjQ4MV5BMl5BanBnXkFtZTgwNzcxOTY5NjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=O-RgquKVTPE")

# Array list that contains all the instances of the movies
movies = [coco, cars, up, finding_dory, inside_out, good_dino]

# Displays all the movies on the web page
fresh_tomatoes.open_movies_page(movies)

