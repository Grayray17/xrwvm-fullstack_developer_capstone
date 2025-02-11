const express = require('express');
const mongoose = require('mongoose');
const fs = require('fs');
const cors = require('cors');
const bodyParser = require('body-parser');
const app = express();
const port = 3030;

app.use(cors());
app.use(bodyParser.json());

const reviewsData = JSON.parse(fs.readFileSync("reviews.json", 'utf8'));
const dealershipsData = JSON.parse(fs.readFileSync("dealerships.json", 'utf8'));

mongoose.connect("mongodb://mongo_db:27017/dealershipsDB", { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log("Connected to MongoDB"))
  .catch(err => console.error("MongoDB connection error:", err));

const Reviews = require('./review');
const Dealerships = require('./dealership');

const seedDatabase = async () => {
  try {
    await Reviews.deleteMany({});
    await Reviews.insertMany(reviewsData['reviews']);
    
    await Dealerships.deleteMany({});
    await Dealerships.insertMany(dealershipsData['dealerships']);

    console.log("Database seeded successfully");
  } catch (error) {
    console.error("Error seeding database:", error);
  }
};
seedDatabase();

// Home Route
app.get('/', (req, res) => res.send("Welcome to the Mongoose API"));

// Fetch all reviews
app.get('/fetchReviews', async (req, res) => {
  try {
    const reviews = await Reviews.find();
    res.json(reviews);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching reviews' });
  }
});

// Fetch reviews by dealer ID
app.get('/fetchReviews/dealer/:id', async (req, res) => {
  try {
    const reviews = await Reviews.find({ dealership: req.params.id });
    res.json(reviews);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching reviews' });
  }
});

// Fetch all dealerships
app.get('/fetchDealers', async (req, res) => {
  try {
    const dealers = await Dealerships.find();
    res.json(dealers);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching dealerships' });
  }
});

// Fetch dealerships by state
app.get('/fetchDealers/:state', async (req, res) => {
  try {
    const dealers = await Dealerships.find({ state: req.params.state });
    res.json(dealers);
  } catch (error) {
    res.status(500).json({ error: `Error fetching dealerships in state ${req.params.state}` });
  }
});

// Fetch dealer by ID using custom id field
app.get('/fetchDealer/:id', async (req, res) => {
  try {
    // Convert the parameter to a number if your IDs are stored as numbers.
    const dealerId = Number(req.params.id);
    const dealer = await Dealerships.findOne({ id: dealerId });
    if (!dealer) return res.status(404).json({ error: 'Dealer not found' });
    res.json(dealer);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching dealer' });
  }
});


// Insert a new review
app.post('/insert_review', express.json(), async (req, res) => {
  try {
    const data = req.body;
    const lastReview = await Reviews.findOne().sort({ id: -1 });
    const newId = lastReview ? lastReview.id + 1 : 1;
    
    const newReview = new Reviews({
      id: newId,
      name: data.name,
      dealership: data.dealership,
      review: data.review,
      purchase: data.purchase,
      purchase_date: data.purchase_date,
      car_make: data.car_make,
      car_model: data.car_model,
      car_year: data.car_year,
    });

    const savedReview = await newReview.save();
    res.json(savedReview);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Error inserting review' });
  }
});

// Start the Express server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
