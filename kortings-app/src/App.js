import React from "react";
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
    const parsedProduct = product.normalize('NFD').replace(/[\u0300-\u036f]/g, '') // Remove accents
		.replace(/([^\w]+|\s+)/g, '-') // Replace space and other characters by hyphen
		.replace(/\-\-+/g, '-')	// Replaces multiple hyphens by one hyphen
		.replace(/(^-+|-+$)/g, ''); 

    return parsedProduct;
  }

  return (
    <div className="App">
      <Routes>
        <Route path="/">
          <Route index element={<Main />} />
          {Offers.map((item) => {
           return <Route path={ "" + item.shop +"?product=" + convertProductToLink(item.product) + ""} element={<SingleProduct item={item} />} />
          })}
        </Route>
      </Routes>
      <Footer/>
    </div>
  );
}

export default App;
