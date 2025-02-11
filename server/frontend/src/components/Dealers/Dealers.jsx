import React, { useState, useEffect } from 'react';
import "./Dealers.css";
import "../assets/style.css";
import Header from '../Header/Header';
import review_icon from "../assets/reviewicon.png";

const Dealers = () => {
  const [dealersList, setDealersList] = useState([]);
  const [states, setStates] = useState([]);

  const backendUrl = process.env.REACT_APP_BACKEND_URL || "http://localhost:8000";

  const getDealers = async () => {
    try {
      const res = await fetch(`${backendUrl}/djangoapp/get_dealers`, { method: "GET" });
      const retobj = await res.json();
      
      if (retobj.status === 200) {
        const allDealers = Array.from(retobj.dealers);
        const uniqueStates = [...new Set(allDealers.map(dealer => dealer.state))];

        setStates(uniqueStates);
        setDealersList(allDealers);
      } else {
        console.error("Error fetching dealers:", retobj.message);
      }
    } catch (error) {
      console.error("Failed to fetch dealers:", error);
    }
  };

  const filterDealers = async (state) => {
    const stateUrl = state === "All" ? `${backendUrl}/djangoapp/get_dealers` : `${backendUrl}/djangoapp/get_dealers/${state}`;

    try {
      const res = await fetch(stateUrl, { method: "GET" });
      const retobj = await res.json();

      if (retobj.status === 200) {
        setDealersList(Array.from(retobj.dealers));
      } else {
        console.error("Error filtering dealers:", retobj.message);
      }
    } catch (error) {
      console.error("Failed to fetch dealers by state:", error);
    }
  };

  useEffect(() => {
    getDealers();
  }, []);

  const isLoggedIn = sessionStorage.getItem("username") !== null;

  return (
    <div>
      <Header />
      <table className="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Dealer Name</th>
            <th>City</th>
            <th>Address</th>
            <th>Zip</th>
            <th>
              <select name="state" id="state" defaultValue="" onChange={(e) => filterDealers(e.target.value)}>
                <option value="" disabled hidden>State</option>
                <option value="All">All States</option>
                {states.map((state, index) => (
                  <option key={index} value={state}>{state}</option>
                ))}
              </select>
            </th>
            {isLoggedIn && <th>Review Dealer</th>}
          </tr>
        </thead>
        <tbody>
          {dealersList.map(dealer => (
            <tr key={dealer.id}>
              <td>{dealer.id}</td>
              <td><a href={`/dealer/${dealer.id}`}>{dealer.full_name}</a></td>
              <td>{dealer.city}</td>
              <td>{dealer.address}</td>
              <td>{dealer.zip}</td>
              <td>{dealer.state}</td>
              {isLoggedIn && (
                <td>
                  <a href={`/postreview/${dealer.id}`}>
                    <img src={review_icon} className="review_icon" alt="Post Review" />
                  </a>
                </td>
              )}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Dealers;
