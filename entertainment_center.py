import media
import fresh_tomatoes

'''
To create a movie instance one needs to provide the name, the storyline for
the movie, a link to the poster, and a youtube link for the trailer
'''

predator = media.Movie("Predator", "Killer alien in the jungle",
                       "https://static.comicvine.com/uploads/original/14/" +
                       "146991/2921588-Hot_Toys_Scar_Predator.jpg",
                       "https://www.youtube.com/watch?v=Y1txEAywdiw")

hardTarget = media.Movie("Hard Target", "Hunters become haunted",
                         "http://res.cloudinary.com/dbm5rx8rl/image/" +
                         "upload/v1496390044/" +
                         "hard-target_8_e3ijtz.jpg",
                         "https://www.youtube.com/watch?v=a_D2PYqk9cM")

revenant = media.Movie("The Revenant", "Survival of an injured  man betrayed" +
                       "by his group", "https://s-media-cache-ak0.pinimg.com" +
                       "/736x/2f/9c/a1/2f9ca1e7b5b42196fc0f6ba668b51757--" +
                       "leonardo-dicaprio-movies--movies.jpg",
                       "https://www.youtube.com/watch?v=QRfj1VCg16Y")

prettyWoman = media.Movie("Pretty Woman", "A broker hires a hooker",
                          "https://i.ytimg.com/vi/sNYalWdtPSA/maxresdefault" +
                          ".jpg",
                          "https://www.youtube.com/watch?v=Wzii8IuL8lk")

stVincent = media.Movie("St. Vincent", "A young boy whose parents just" +
                        "divorced meets a bawdy war veteran",
                        "http://www.technologytell.com" +
                        "/entertainment/files/2014/10/vincent-trio.jpg",
                        "https://www.youtube.com/watch?v=9dP5lJnJHXg")

captainPhilips = media.Movie("Captain Philips", "An intense interaction" +
                             "between Captain Richard Philips and" +
                             " Somali pirate captain",
                             "http://www.fatmovieguy.com/wp-content/uploads" +
                             "/2013/09/Captain-Phillips-Image-1.jpg",
                             "https://www.youtube.com/watch?v=pV-ptQX-75Y")

wonderWoman = media.Movie("Wonder Woman", "A woman fighting wars" +
                          " alongside men",
                          "http://cdn.collider.com/wp-content/uploads" +
                          "/2017/03/justice-league-wonder-woman-poster.jpg",
                          "https://www.youtube.com/watch?v=VSB4wGIdDwo")

mummy = media.Movie("The Mummy", "An ancient princess wakes up and " +
                    "brings terror with her",
                    "https://www.flickeringmyth.com/wp-content/uploads" +
                    "/2017/04/Mummy-images-2-600x395.jpg",
                    "https://www.youtube.com/watch?v=IjHgzkQM2Sg")

alien = media.Movie("Alien: Covenant", "The space crew lands on an unknown " +
                    "planet and faces threats beyond their imagination",
                    "https://i.kinja-img.com/gawker-media/image/upload/" +
                    "s---8XOZgKk--/c_scale,fl_progressive,q_80,w_800/" +
                    "l5cgyu7dbva6fzldy1d3.jpg",
                    "https://www.youtube.com/watch?v=H0VW6sg50Pk")

# making a list of the movies
movies_list = [predator, hardTarget, revenant, prettyWoman, stVincent,
               captainPhilips, wonderWoman, mummy, alien]

# calling html file to open a movies trailer website
fresh_tomatoes.open_movies_page(movies_list)

#predator.show_trailer()
