import { Link } from "react-router-dom";
import localForage from 'localforage'
import React, {useState, useEffect } from "react";

function SearchButton(props) {
    
    useEffect(() => {
    },[])

    return (
        <div className="button-cell">
           <Link to="/zoek"><div className="button search-button">
            <i class="ri-search-line"></i>
            <div className="button-tag">zoek</div>
            </div></Link> 
        </div>
    )
  }
  
  export default SearchButton;
    