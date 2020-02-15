// This is a class for utilities, like calculating scores
public class Utils {
    public static double getScore (int numRelevantTags, int numDislikedTags) {
        return min(100, max(0, max(10 * numRelevantTags, 100) + max(-10 * numDislikedTags, -100)));
    }

    public void printList(Anime[] animeList) {
        int length = length(animeList);
        for (int i = 0; i < length; i++) {
            System.out.println("Title: " + animeList[i].title);
            System.out.println("Score: " + animeList[i].score);
            System.out.println("Description: " + animeList[i].description);
            System.out.println("Type: " + animeList[i].type);
            System.out.println("AkScore: " + animeList[i].AkScore);
            System.out.println("Genres: " + animeList[i].genres);
            System.out.println("\n");
        }
    }
}