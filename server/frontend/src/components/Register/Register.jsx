import React, { useState } from "react";
import "./Register.css";
import user_icon from "../assets/person.png";
import email_icon from "../assets/email.png";
import password_icon from "../assets/password.png";
import close_icon from "../assets/close.png";
import { useNavigate } from "react-router-dom";

const Register = () => {
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const navigate = useNavigate();

  const register = async (e) => {
    e.preventDefault();
    let register_url = window.location.origin + "/djangoapp/registration"; // URL of the registration endpoint

    const res = await fetch(register_url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userName,
        password,
        firstName,
        lastName,
        email,
      }),
    });

    const json = await res.json();
    if (json.status) {
      sessionStorage.setItem("username", json.userName);
      window.location.href = window.location.origin; // Redirect to home page
    } else if (json.error === "Already Registered") {
      alert("The user with the same username is already registered");
      window.location.href = window.location.origin; // Redirect to home page
    }
  };

  return (
    <div className="register_container" style={{ width: "50%" }}>
      <div
        className="header"
        style={{ display: "flex", flexDirection: "row", justifyContent: "space-between" }}
      >
        <span className="text" style={{ flexGrow: "1" }}>
          SignUp
        </span>
        <div style={{ display: "flex", flexDirection: "row", justifySelf: "end", alignSelf: "start" }}>
          <a
            href="/"
            onClick={() => {
              navigate("/");
            }}
            style={{ justifyContent: "space-between", alignItems: "flex-end" }}
          >
            <img style={{ width: "1cm" }} src={close_icon} alt="X" />
          </a>
        </div>
        <hr />
      </div>
      <form onSubmit={register}>
        <div className="inputs">
          <div className="input">
            <img src={user_icon} className="img_icon" alt="First Name" />
            <input
              type="text"
              name="first_name"
              placeholder="First Name"
              className="input_field"
              onChange={(e) => setFirstName(e.target.value)}
              required
            />
          </div>
          <div>
            <img src={user_icon} className="img_icon" alt="Last Name" />
            <input
              type="text"
              name="last_name"
              placeholder="Last Name"
              className="input_field"
              onChange={(e) => setLastName(e.target.value)}
              required
            />
          </div>
          <div>
            <img src={email_icon} className="img_icon" alt="Email" />
            <input
              type="email"
              name="email"
              placeholder="Email"
              className="input_field"
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="input">
            <img src={user_icon} className="img_icon" alt="Username" />
            <input
              type="text"
              name="username"
              placeholder="Username"
              className="input_field"
              onChange={(e) => setUserName(e.target.value)}
              required
            />
          </div>
          <div className="input">
            <img src={password_icon} className="img_icon" alt="Password" />
            <input
              type="password"
              name="password"
              placeholder="Password"
              className="input_field"
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
        </div>
        <div className="submit_panel">
          <input className="submit" type="submit" value="Register" />
        </div>
      </form>
      <div className="text-center mt-3">
        <a href="/login" className="btn btn-link">
          Already have an account? Login here
        </a>
      </div>
    </div>
  );
};

export default Register;
