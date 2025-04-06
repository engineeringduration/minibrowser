const express = require("express");
const cors = require("cors");
const axios = require("axios");

const app = express();
app.use(cors());

app.get("/proxy", async (req, res) => {
  try {
    const url = req.query.url; // Example: /proxy?url=https://example.com
    const response = await axios.get(url, { headers: { "User-Agent": "Mozilla/5.0" } });
    res.send(response.data);
  } catch (error) {
    res.status(500).send("Error fetching content.");
  }
});

app.listen(3000, () => console.log("Proxy running on port 3000"));
