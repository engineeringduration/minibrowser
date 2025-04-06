// public class Main {
//     public static void main(String[] args) {
//         System.out.println("Search Engine UI Starting...");
//         SearchUI ui = new SearchUI();
//         ui.setVisible(true);
//     }
// }
import javax.swing.SwingUtilities;

public class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            SearchUI ui = new SearchUI();
            ui.setVisible(true);
        });
    }
}
