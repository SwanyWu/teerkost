import { Link } from "react-router-dom";
import React, {useState, useEffect } from "react";

function GoHomeButton(props) {

    return (
        <div className="button-cell">
        <Link to="/"><div className="button home-button">
            <i class="ri-home-line"></i>
            <div className="button-tag">teerkost</div>
        </div></Link>
        </div>
    )
  }
  
  export default GoHomeButton;
    