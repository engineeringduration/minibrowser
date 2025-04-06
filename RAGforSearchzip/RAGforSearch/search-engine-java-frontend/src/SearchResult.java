public class SearchResult {
    private String url;
    private String title;
    private String description;
    private double distance;

    public SearchResult(String url, String title, String description, double distance) {
        this.url = url;
        this.title = title;
        this.description = description;
        this.distance = distance;
    }

    public String getUrl() {
        return url;
    }

    public String getTitle() {
        return title;
    }

    public String getDescription() {
        return description;
    }

    public double getDistance() {
        return distance;
    }
}
