import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import org.json.JSONArray;
import org.json.JSONObject;

public class ApiClient {

    private static final String BASE_URL = "http://localhost:5000/search";

    // Fetch search results using API
    public static List<SearchResult> fetchResults(String query, int page, int perPage) {
        List<SearchResult> results = new ArrayList<>();
        HttpURLConnection connection = null;
        BufferedReader reader = null;

        try {
            // Encode query to handle spaces and special characters
            String encodedQuery = URLEncoder.encode(query, StandardCharsets.UTF_8.toString());

            // Construct API URL
            String apiUrl = String.format("%s?query=%s&page=%d&per_page=%d", BASE_URL, encodedQuery, page, perPage);
            System.out.println("Connecting to API: " + apiUrl);

            URL url = new URL(apiUrl);
            connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Accept", "application/json");

            int responseCode = connection.getResponseCode();
            if (responseCode != 200) {
                System.out.println("Error: API responded with status code " + responseCode);
                return results;
            }

            // Read response from API
            reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            StringBuilder response = new StringBuilder();
            String line;
            
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }

            // Parse JSON response
            JSONObject jsonResponse = new JSONObject(response.toString());
            JSONArray jsonArray = jsonResponse.getJSONArray("results");

            // Convert JSON to SearchResult objects
            for (int i = 0; i < jsonArray.length(); i++) {
                JSONObject obj = jsonArray.getJSONObject(i);
                results.add(new SearchResult(
                        obj.getString("url"),
                        obj.getString("title"),
                        obj.getString("description"),
                        obj.getDouble("distance")
                ));
            }
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            try {
                if (reader != null) reader.close();
                if (connection != null) connection.disconnect();
            } catch (Exception e) {
                System.out.println("Cleanup Error: " + e.getMessage());
            }
        }
        return results;
    }
}
