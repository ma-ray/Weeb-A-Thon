// Object for the anime!
public class Anime {
    private String name, type, description;
    private BufferedImage object;
    private double score;
    private String genres[];
    private int AkScore;

    public Anime(String name, BufferedImage object, double score, String genres[], String description,String type,int AkScore) {
        this.name = name;
        this.object = object;
        this.score = score;
        this.description = description;
        this.type = type; 
        this.AkScore = AkScore;
        this.genres = genres;

    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public BufferedImage getObject() {
        return object;
    }

    public void setObject(BufferedImage object) {
        this.object = object;
    }

    public double getScore() {
        return score;
    }

    public void setScore(double score) {
        this.score = score;
    }

    public String[] getGenres() {
        return genres;
    }

    public void setGenres(String[] genres) {
        this.genres = genres;
    }

    public int getAkScore() {
        return AkScore;
    }

    public void setAkScore(int akScore) {
        AkScore = akScore;
    }
}