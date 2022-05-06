import { Link } from "react-router-dom";
import localForage from 'localforage'
import React, {useState, useEffect } from "react";

function SearchButton(props) {
    
    useEffect(() => {
    },[])

    return (
        <div className="button-cell">
            <div className="button search-button">
            <i class="ri-search-line"></i>
            <div className="search-button-tag">zoek</div>
            </div>
        </div>
    )
  }
  
  export default SearchButton;
    