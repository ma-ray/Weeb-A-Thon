// This is a class for utilities, like calculating scores
public class Utils {
    public static double getScore (int numRelevantTags, int numDislikedTags) {
        return min(100, max(0, max(10 * numRelevantTags, 100) + max(-10 * numDislikedTags, -100)));
    }
}