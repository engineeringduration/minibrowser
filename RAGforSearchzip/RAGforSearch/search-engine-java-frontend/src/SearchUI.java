import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.List;

public class SearchUI extends JFrame {

    private JTextField searchField;
    private JButton searchButton;
    private JPanel resultPanel;
    private JLabel paginationLabel;
    private JButton prevPageButton, nextPageButton;
    private int currentPage = 1;
    private final int RESULTS_PER_PAGE = 5;

    public SearchUI() {
        setTitle("AI Search Engine");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Header Section
        JPanel headerPanel = new JPanel(new FlowLayout());

        searchField = new JTextField(40);
        searchButton = new JButton("Search");

        headerPanel.add(searchField);
        headerPanel.add(searchButton);
        add(headerPanel, BorderLayout.NORTH);

        // Results Section
        resultPanel = new JPanel();
        resultPanel.setLayout(new BoxLayout(resultPanel, BoxLayout.Y_AXIS));
        JScrollPane scrollPane = new JScrollPane(resultPanel);
        add(scrollPane, BorderLayout.CENTER);

        // Pagination Controls
        JPanel paginationPanel = new JPanel(new FlowLayout());
        prevPageButton = new JButton("Previous");
        nextPageButton = new JButton("Next");
        paginationLabel = new JLabel("Page: 1");

        prevPageButton.setEnabled(false);
        paginationPanel.add(prevPageButton);
        paginationPanel.add(paginationLabel);
        paginationPanel.add(nextPageButton);
        add(paginationPanel, BorderLayout.SOUTH);

        // Listeners
        searchButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                currentPage = 1;
                performSearch();
            }
        });

        prevPageButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (currentPage > 1) {
                    currentPage--;
                    performSearch();
                }
            }
        });

        nextPageButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                currentPage++;
                performSearch();
            }
        });
    }

    private void performSearch() {
        String query = searchField.getText().trim();
        if (query.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Please enter a search query.");
            return;
        }

        List<SearchResult> results = ApiClient.fetchResults(query, currentPage, RESULTS_PER_PAGE);
        resultPanel.removeAll();

        if (results.isEmpty()) {
            resultPanel.add(new JLabel("No results found."));
            nextPageButton.setEnabled(false);
        } else {
            for (SearchResult result : results) {
                JPanel card = new JPanel(new BorderLayout());
                card.setBorder(BorderFactory.createLineBorder(Color.GRAY));
                card.setBackground(Color.WHITE);
                card.setPreferredSize(new Dimension(700, 100));

                JLabel titleLabel = new JLabel("<html><a href='" + result.getUrl() + "'>" + result.getTitle() + "</a></html>");
                titleLabel.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
                titleLabel.addMouseListener(new java.awt.event.MouseAdapter() {
                    public void mouseClicked(java.awt.event.MouseEvent e) {
                        try {
                            Desktop.getDesktop().browse(new java.net.URI(result.getUrl()));
                        } catch (Exception ex) {
                            ex.printStackTrace();
                        }
                    }
                });

                JLabel descriptionLabel = new JLabel("<html>" + result.getDescription() + "</html>");

                card.add(titleLabel, BorderLayout.NORTH);
                card.add(descriptionLabel, BorderLayout.CENTER);
                resultPanel.add(card);
            }
            nextPageButton.setEnabled(results.size() == RESULTS_PER_PAGE);
        }

        paginationLabel.setText("Page: " + currentPage);
        prevPageButton.setEnabled(currentPage > 1);
        resultPanel.revalidate();
        resultPanel.repaint();
    }
}


/*
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.List;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.net.URI;
import com.formdev.flatlaf.FlatIntelliJLaf;

public class SearchUI extends JFrame {

    private JTextField searchField;
    private JButton searchButton;
    private JPanel resultPanel;
    private JLabel paginationLabel;
    private JButton prevPageButton, nextPageButton;
    private int currentPage = 1;
    private final int RESULTS_PER_PAGE = 5;

    public SearchUI() {
        try {
            UIManager.setLookAndFeel(new FlatIntelliJLaf()); // Modern Look
        } catch (Exception e) {
            e.printStackTrace();
        }

        setTitle("AI Search Engine");
        setSize(900, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // 🟢 Header Section (Search Bar)
        JPanel headerPanel = new JPanel(new FlowLayout());
        headerPanel.setBackground(new Color(30, 144, 255));

        searchField = new JTextField(40);
        searchField.setFont(new Font("Segoe UI", Font.PLAIN, 16));

        searchButton = new JButton("🔎 Search");
        searchButton.setBackground(new Color(0, 123, 255));
        searchButton.setForeground(Color.WHITE);

        headerPanel.add(searchField);
        headerPanel.add(searchButton);
        add(headerPanel, BorderLayout.NORTH);

        // 🟢 Results Section (Scrollable)
        resultPanel = new JPanel();
        resultPanel.setLayout(new BoxLayout(resultPanel, BoxLayout.Y_AXIS));
        resultPanel.setBackground(Color.WHITE);

        JScrollPane scrollPane = new JScrollPane(resultPanel);
        scrollPane.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        add(scrollPane, BorderLayout.CENTER);

        // 🟢 Pagination Controls
        JPanel paginationPanel = new JPanel(new FlowLayout());
        prevPageButton = new JButton("⬅ Previous");
        nextPageButton = new JButton("Next ➡");
        paginationLabel = new JLabel("Page: 1");
        paginationLabel.setFont(new Font("Segoe UI", Font.BOLD, 14));

        prevPageButton.setEnabled(false);
        paginationPanel.add(prevPageButton);
        paginationPanel.add(paginationLabel);
        paginationPanel.add(nextPageButton);
        add(paginationPanel, BorderLayout.SOUTH);

        // 🟢 Listeners
        searchButton.addActionListener(e -> {
            currentPage = 1;
            performSearch();
        });

        prevPageButton.addActionListener(e -> {
            if (currentPage > 1) {
                currentPage--;
                performSearch();
            }
        });

        nextPageButton.addActionListener(e -> {
            currentPage++;
            performSearch();
        });
    }

    // 📌 Perform Search
    private void performSearch() {
        String query = searchField.getText().trim();
        if (query.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Please enter a search query.", "Warning", JOptionPane.WARNING_MESSAGE);
            return;
        }

        List<SearchResult> results = ApiClient.fetchResults(query, currentPage, RESULTS_PER_PAGE);
        resultPanel.removeAll();

        if (results.isEmpty()) {
            resultPanel.add(new JLabel("⚠ No results found."));
            nextPageButton.setEnabled(false);
        } else {
            for (SearchResult result : results) {
                JPanel card = createResultCard(result);
                resultPanel.add(card);
            }
            nextPageButton.setEnabled(results.size() == RESULTS_PER_PAGE);
        }

        paginationLabel.setText("Page: " + currentPage);
        prevPageButton.setEnabled(currentPage > 1);
        resultPanel.revalidate();
        resultPanel.repaint();
    }

    // 📌 Create Result Card UI
    private JPanel createResultCard(SearchResult result) {
        JPanel card = new JPanel(new BorderLayout());
        card.setBorder(BorderFactory.createLineBorder(new Color(220, 220, 220)));
        card.setBackground(Color.WHITE);
        card.setPreferredSize(new Dimension(800, 120));

        // Title with Link
        JLabel titleLabel = new JLabel("<html><a href='#'>" + result.getTitle() + "</a></html>");
        titleLabel.setFont(new Font("Segoe UI", Font.BOLD, 16));
        titleLabel.setForeground(new Color(30, 144, 255));
        titleLabel.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));

        titleLabel.addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent e) {
                try {
                    Desktop.getDesktop().browse(new URI(result.getUrl()));
                } catch (Exception ex) {
                    ex.printStackTrace();
                }
            }
        });

        // Description
        JLabel descriptionLabel = new JLabel("<html>" + result.getDescription() + "</html>");
        descriptionLabel.setFont(new Font("Segoe UI", Font.PLAIN, 14));

        card.add(titleLabel, BorderLayout.NORTH);
        card.add(descriptionLabel, BorderLayout.CENTER);
        return card;
    }
}
*/