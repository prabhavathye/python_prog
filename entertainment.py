import fresh_tomatoes
import media

terminator_genisys = media.Movie("Terminator Genisys",
                                 "John sends Kyle to the year 1984 to protect his mother Sarah from being killed.When the timeline is altered, Kyle asks her to travel to the year 2017 to stop an AI system that wants to wipe mankind",
                                 "https://upload.wikimedia.org/wikipedia/en/b/bc/Terminator_Genisys.JPG",
                                 "https://www.youtube.com/watch?v=jNU_jrPxs-0"
                              )
#print(terminator_genisys.storyline)
starwars = media.Movie("Star Wars",
                       "Although 2015 includes Avengers 2, the 7th Furious and the last Hunger Games, Star Wars 7 will conquer the best new movie list 2015 in Hollywood and make it the most anticipated return, attributing to its darker tone, grittier visuals and the characters like Mark Hamill, Harrison Ford we all love. The blockbuster is a continuation of the saga created by George Lucas set 30 years after Episode VI. ",
                       "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                       "https://www.youtube.com/watch?v=rRLYSzQ-7uo")
#print(starwars.storyline)
#starwars.show_trailer()
mission_impossible=media.Movie("Mission Impossible",
                               "Ethan and team take on their most impossible mission yet, eradicating the Syndicate - an International rogue organization as highly skilled as they are, committed to destroying the IMF. ",
                               "https://upload.wikimedia.org/wikipedia/en/f/fb/Mission_Impossible_Rogue_Nation_poster.jpg",
                               "https://www.youtube.com/watch?v=EIsauUFIguE")
spectre = media.Movie("Spectre",
                      "A cryptic message from Bond's past sends him on a trail to uncover a sinister organization. While M battles political forces to keep the secret service alive, Bond peels back the layers of deceit to reveal the terrible truth behind SPECTRE. ",
                      "https://upload.wikimedia.org/wikipedia/en/c/c3/Spectre_poster.jpg",
                      "https://www.youtube.com/watch?v=7GqClqvlObY")
xmen_apocalypse=media.Movie("X-men Apocalypse",
                            "After the re-emergence of the world's first mutant, world-destroyer Apocalypse, the X-Men must unite to defeat his extinction level plan. ",
                            "https://upload.wikimedia.org/wikipedia/en/0/04/X-Men_-_Apocalypse.jpg",
                            "https://www.youtube.com/watch?v=PfBVIHgQbYk")
captain_american_civilwar = media.Movie("Captain American Civil War",
                                       "Political interference in the Avengers' activities causes a rift between former allies Captain America and Iron Man. ",
                                       "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
                                       "https://www.youtube.com/watch?v=xnv__ogkt0M")
movies = [terminator_genisys,starwars,mission_impossible,spectre,xmen_apocalypse,captain_american_civilwar]
fresh_tomatoes.open_movies_page(movies)                    


