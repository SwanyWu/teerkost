import React from "react";
import 'remixicon/fonts/remixicon.css'
import './App.css';
import { Routes, Route } from "react-router-dom";
import Footer from './Footer';
import Main from './Main';
import Bookmarks from './Bookmarks';
import SingleProduct from './SingleProduct';
import Offers from './offers.json';
import NotFound from "./NotFound";

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

  const shops = ["jumbo", "aldi", "ah", "lidl", "ekoplaza"]
  const categories = [
    "bier", "groente", "vlees", "vis", "fruit", 
    "zuivel", "wijn", "vegan", "kant-en-klaar", 
    "aardappel", "brood", "kaas", 
    "koffie", "thee", "beleg", "ontbijt",
    "noten", "frisdrank", "ijs", "pasta", "chocola", 
    "chips", "koek", "snoep", "verzorging", "huishouden"
  ]

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
          
          <Route path="bewaard" element={<Bookmarks />} />
          <Route path="*" element={<NotFound/>} />
        </Route>
      </Routes>
      <Footer/>
    </div>
  );
}

export default App;
