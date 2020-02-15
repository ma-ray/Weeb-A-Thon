package swing;


import java.awt.image.BufferedImage;

// Object for the anime!
public class User {
    private String name;
    private String likedGenres[];
    private String dislikedGenres[];

    public User() {

    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String[] getLikedGenres() {
        return likedGenres;
    }

    public void setLikedGenres(String[] likedGenres) {
        this.likedGenres = likedGenres;
    }

    public String[] getDislikedGenres() {
        return dislikedGenres;
    }


    public void setDislikedGenres(String[] dislikedGenres) {
        this.dislikedGenres = dislikedGenres;
    }

    public void getNumDisliked(String[] animeGenres, String[] personalDislikes) {
        this.dislikedGenres = animeGenres;

        String currentAnimeGenre = "";
        String currentPersonalDislikes = "";

        int counter = 0;
        int animeGenreLength = animeGenres.length;
        int personalDislikesLength = personalDislikes.length;

        for (int i = 0; i < animeGenreLength; i++) {
            currentAnimeGenre = animeGenres[i];
            for (int j = 0; j < personalDislikesLength; j++) {
                currentPersonalDislikes = personalDislikes[j];


            }
        }

    }
}