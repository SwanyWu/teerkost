import React from "react";
import 'remixicon/fonts/remixicon.css'
import './App.css';
import { Routes, Route } from "react-router-dom";
import Footer from './Footer';
import Main from './Main';
import SingleProduct from './SingleProduct';
import Counter from './Counter';
import Offers from './offers.json';


function App() {
  
  const convertProductToLink = (product) => {
    product = product.trim();
    var parsedProduct = product.normalize('NFD').replace(/[\u0300-\u036f]/g, '') // Remove accents
		.replace(/([^\w]+|\s+)/g, '-') // Replace space and other characters by hyphen
		.replace(/\-\-+/g, '-')	// Replaces multiple hyphens by one hyphen
		.replace(/(^-+|-+$)/g, ''); 
    
    parsedProduct = parsedProduct.toLowerCase(); 

    return parsedProduct;
  }

  const shops = ["jumbo", "aldi", "ah", "lidl"]
  const categories = ["bier", "koffie", "groente", "vis", "fruit", 
  "kant-en-klaar", "wijn", "aardappel", "brood", "beleg", "kaas", 
  "noten", "zuivel", "vlees", "frisdrank", "chocola", "chips", "koek", "verzorging", "huishouden"]

  return (
    <div className="App">
      <Routes>
        <Route path="/">
          <Route index element={<Main />} />

          {Offers.map((item) => { // Map all routes to the offers
           return <Route path={ "" + item.shop +"/product/" + convertProductToLink(item.product) + ""} element={<SingleProduct item={item} />} />
          })}

          {shops.map((shop, key) => { // Map all routes for shops
            return <Route key={key} path={shop} element={<Main shop={shop} />} />
          })}

          {shops.map((shop) => { // Map all routes for shops and categories
            return categories.map((category, key) => {
              return <Route key={key} path={shop + "/" + category} element={<Main shop={shop} cat={category} />} />
            })
          })}

          {categories.map((category, key) => { // Map all routes for categories for all shops
              return <Route key={key} path={"alle-winkels/" + category} element={<Main cat={category} />} />
            })}
          
          <Route path="alle-winkels" element={<Main />} /> { /* Map all routes for all shops with everything */ }

        </Route>
      </Routes>
      <Footer/>
    </div>
  );
}

export default App;
